import React from "react";
import { UserConsumer } from "./UserContext";
import { DateTime, Duration } from "luxon";

// TODO @ben and @ishaan get this from the backend db
const CLOCK_INTERVAL = 1000;
const AVAILABLE_DISPLAY_VALUE = "-";
const STATUS_TYPES = { FOCUS: "focus", AVAILABLE: "available", OFF: "off" };

class Clock extends React.Component {
  constructor(props) {
    super(props);
    this.timerID = 0;
    this.state = {
      active: true,
      statusType: undefined,
      timeDisplayValue: AVAILABLE_DISPLAY_VALUE,
      progress: 1,
      running: false
    };
  }

  handleStartStopClick = () => {
    console.log("handleStartStopClick");
    // start or stop focus timer
    const newState = !this.props.focusTimerRunning; //TODO: can remove these two lines and move the logic into the if
    const statusType = newState ? STATUS_TYPES.FOCUS : STATUS_TYPES.AVAILABLE;
    if (statusType == STATUS_TYPES.FOCUS) {
      this.startTimer();
      this.props.handleFocusTimerChange(STATUS_TYPES.FOCUS);
    } else if (statusType == STATUS_TYPES.AVAILABLE) {
      this.stopAndClearTimer();
      this.props.handleFocusTimerChange(STATUS_TYPES.AVAILABLE);
    }
  };

  handleOnOffClick = () => {
    console.log("handleOnOffClick");
    let newState = !this.state.active;
    this.setState({ active: newState });
    const statusType = newState ? STATUS_TYPES.AVAILABLE : STATUS_TYPES.OFF;
    this.props.postToStatusRoute({ statusType: statusType });
    if (statusType == STATUS_TYPES.OFF) {
      // This is a hack, otherwise we need to do a bunch of refactoring
      this.props.handleFocusTimerChange(STATUS_TYPES.AVAILABLE, false);
      this.stopAndClearTimer();
    }
  };
  startTimer = () => {
    this.timerID = setInterval(this.countDown, CLOCK_INTERVAL);
    console.log("startTimer", this.timerID, this.state.timeDisplayValue);
    this.setState({ running: true });
  };

  stopAndClearTimer() {
    clearInterval(this.timerID);
    this.setState({
      timeDisplayValue: AVAILABLE_DISPLAY_VALUE,
      running: false,
      progress: 1
    });
  }

  countDown = () => {
    const now = DateTime.utc();
    const length = this.props.focusTimerLength;
    const end = this.props.assumedEndTime;
    try {
      const diff = now.diff(end); //diffNow doesn't seem to work
      const displayValue = formatDurationForDisplay(diff);
      const barPC =
        Math.abs(diff.as("milliseconds")) / length.as("milliseconds");
      this.setState({
        timeDisplayValue: displayValue,
        progress: barPC,
        diff: diff
      });
      if (diff >= 0) {
        // diff is a duration in negative miliseconds when compared with >=
        // no longer runing
        this.props.handleFocusTimerChange(STATUS_TYPES.AVAILABLE, false);
        this.stopAndClearTimer();
      }
    } catch (e) {
      throw e;
    }
  };

  handleKeyPress = e => {
    const ENTER = 13;
    console.log("pressed:", e.keyCode);
    // const SPACE = 32;
    if (e.keyCode == ENTER && e.target.id == "ActionTapTarget") {
      // console.log("you pressed enter on ActionTapTarget");
      this.handleStartStopClick();
    } else if (e.keyCode == ENTER && e.target.id == "OnOffButton") {
      // console.log("you pressed enter on OnOffButton");
      this.handleOnOffClick();
    }
  };

  setDashArray = () => {
    const ringLength = this.progressRingClosed;
    let dashLength = this.state.progress * ringLength;
    return `${Math.round(dashLength)} ${ringLength}`;
    //Rounding the dash length should save a few renders
  };

  colourForStart = "#029245";
  colourForStop = "#E10000";
  messageForStart = "Start";
  messageForStop = "Stop";

  progressRingClosed = 655;
  progressRingZero = 0;

  render() {
    if (
      this.props.focusTimerRunning &&
      !this.state.running &&
      (this.state.diff < 0 || typeof this.state.diff == "undefined")
    ) {
      this.startTimer(); //TODO: this should probably be in a shouldRender
    }
    return (
      <div>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          id="Clock"
          viewBox="0 0 249.8 249.6"
          className="clock"
        >
          <g id="theClock" opacity={this.state.active ? 1 : 0.1}>
            <path
              id="bed"
              fill="#fff"
              opacity=".3"
              d="M125 .1h103.4a21.3 21.3 0 0 1 21.2 21.3v103.4A124.7 124.7 0 1 1 125 .1"
            />
            <g
              id="ActionTapTarget"
              onClick={this.handleStartStopClick}
              onKeyDown={this.handleKeyPress}
              tabIndex="0"
              role="button"
            >
              <circle
                cx="125.8"
                cy="125.9"
                r="95.6"
                fill="#ffffff03"
                stroke="none"
              />
              <path
                id="ActionBackground"
                fill={
                  this.props.focusTimerRunning
                    ? this.colourForStop
                    : this.colourForStart
                }
                d="M37.2 159.4a95.6 95.6 0 0 0 179 0z"
              />
              <text
                fill="#fff"
                fontSize="19.8"
                textAnchor="middle"
                transform="translate(125.8 184.5)"
              >
                {this.props.focusTimerRunning
                  ? this.messageForStop
                  : this.messageForStart}
              </text>
            </g>
            <circle
              id="InnerRing"
              cx="125.8"
              cy="125.9"
              r="95.6"
              fill="none"
              stroke="#b3b2b2"
              strokeWidth="13"
            />
            <text
              fill="#010101"
              fontSize="70"
              textAnchor="middle"
              transform="translate(129 132)"
            >
              {this.state.timeDisplayValue}
            </text>
            <path
              id="ProgressRing"
              fill="none"
              stroke="#4a494a"
              strokeDasharray={this.setDashArray()}
              strokeLinecap="round"
              strokeWidth="13"
              d="M126.4 20.5a104.6 104.6 0 1 1-.6 0"
            />
          </g>
          <g
            id="OnOffButton"
            onClick={this.handleOnOffClick}
            onKeyDown={this.handleKeyPress}
            tabIndex="0"
            role="button"
          >
            <circle
              id="OnOffTapTarget"
              cx="228.4"
              cy="20.5"
              r="19.5"
              fill="#fff"
              opacity=".1"
            />
            <path
              d="M224.1 10.3a11.9 11.9 0 1 0 8.5 0M228.4 4.1v14"
              fill="none"
              stroke="black"
              strokeLinecap="round"
              strokeWidth="2px"
            />
          </g>
        </svg>
        <div className="debug">
          {/* <input
            type="range"
            id="ClockProgress"
            min="0"
            max="1"
            step="0.01"
            value={this.state.progress}
            onChange={e => {
              this.setState({ progress: e.target.value });
            }}
          /> */}
          <pre>
            state:
            {JSON.stringify(this.state, null, 2)}
            props:
            {JSON.stringify(this.props, null, 2)}
            localStartTime:
            {DateTime.fromISO(this.props.startTime, { zone: "utc" })
              .toLocal()
              .toISO()}
          </pre>
        </div>
      </div>
    );
  }
}

class ClockWithContext extends React.Component {
  // constructor(props) {
  //   super(props);
  // }
  render() {
    return (
      <UserConsumer>
        {context => {
          console.log("context", context);
          if (!context.userCpeId) {
            return (
              <div>
                <h2>No light ID</h2>
                <p>
                  There&apos;s a number on the back of your light. Go to the
                  settings page and enter it into the box for{" "}
                  <strong>Light ID</strong>
                </p>
              </div>
            );
          } else {
            return (
              <Clock
                {...this.props}
                idToken={context.idToken}
                focusTimerRunning={context.focusTimerRunning}
                handleStatusIdChange={context.handleStatusIdChange}
                handleFocusTimerChange={context.handleFocusTimerChange}
                focusTimerLength={context.focusTimerLength}
                postToStatusRoute={context.postToStatusRoute}
                // timer specific
                // closed={thisttt_closed}
                timerId={context.tt_timerId}
                interruptions={context.tt_interruptions}
                rating={context.tt_rating}
                startTime={context.tt_startTime}
                statusType={context.tt_statusType}
                // assumedEndTime={context.tt_assumedEndTime}
                actualEndTime={context.tt_actualEndTime}
                localStartTime={context.debug_startTimeAsLocal}
              />
            );
          }
        }}
      </UserConsumer>
    );
  }
}

function formatDurationForDisplay(diff) {
  const positive = Duration.fromMillis(Math.abs(diff.milliseconds));
  return positive.toFormat("m:ss");
}

export { ClockWithContext, Clock };
