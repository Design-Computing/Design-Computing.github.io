import React from "react";
import ReactDOM from "react-dom";
import { create } from "react-test-renderer";
import { Clock } from "../Clock";
import { ClockWithContext } from "../Clock";

test("renders without crashing", () => {
  const div = document.createElement("div");
  ReactDOM.render(<ClockWithContext />, div);
});

test("renders without crashing", () => {
  const div = document.createElement("div");
  ReactDOM.render(<Clock />, div);
});

test("Clock snapshot", () => {
  const c = create(<Clock />).toJSON();
  expect(c).toMatchSnapshot();
});

test("ClockWithContext snapshot", () => {
  const c = create(<ClockWithContext />).toJSON();
  expect(c).toMatchSnapshot();
});

test("Can get instance of ClockWithContext", () => {
  const c = create(<ClockWithContext />);
  const instance = c.getInstance();
  expect(instance).toBeTruthy();
});

test("Can get instance of Clock", () => {
  const c = create(<Clock />);
  const instance = c.getInstance();
  expect(instance).toBeTruthy();
});

test("off button toggles state", () => {
  const c = create(
    <Clock
      actualEndTime={"2019-05-15T23:21:58.644Z"}
      focusTimerLength={"PT1500S"}
      focusTimerRunning={false}
      handleFocusTimerChange={() => {}}
      handleStatusIdChange={() => {}}
      idToken={"aLongHash"}
      interruptions={0}
      localStartTime={"2019-05-15T23:21:58.644Z"}
      postToStatusRoute={() => {}}
      rating={0}
      startTime={"2019-05-15T23:21:58.644Z"}
      statusType={"focus"}
      timerId={100}
    />
  );
  const instance = c.getInstance();
  instance;
  // TODO figure out how to test these
  // maybe we remove context altogether
  expect(instance.state.active).toBe(true);
  instance.handleOnOffClick();
  expect(instance.state.active).toBe(false);
  instance.handleOnOffClick();
  expect(instance.state.active).toBe(true);
});

test("start button toggles running", () => {
  // TODO create test to see if parent state changes
  const c = create(<Clock />);
  c;
});
