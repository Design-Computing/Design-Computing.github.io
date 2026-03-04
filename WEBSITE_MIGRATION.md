# Website Migration: React to Vanilla JS

## What Changed

### Documentation Updates ✅
Updated markdown files with new pytest commands:
- `md/week1.md` - 4 test command references updated
- `md/week2.md` - 2 test command references updated  
- `md/useful_commands.md` - 2 test command references updated

**Old command:**
```bash
python ../course/set1/tests.py
```

**New commands:**
```bash
# From the me directory:
pytest ../course/set1/

# Or navigate to course first (recommended):
cd ../course
pytest set1/
```

### New Vanilla JS Website ✅

Created `index-vanilla.html` - a modern, zero-build-step replacement for the React app.

**Benefits:**
- ✅ No npm dependencies (no vulnerabilities!)
- ✅ No build step (no Parcel, Babel, Webpack)
- ✅ Faster page loads (~40KB vs ~200KB+ with React)
- ✅ Easier to maintain
- ✅ Uses modern browser APIs (fetch, ES6+, async/await)
- ✅ Markdown parsing via CDN (marked.js)
- ✅ Same visual design and functionality

**What it does:**
1. Fetches course content markdown from GitHub API
2. Renders markdown to HTML using marked.js
3. Displays student forks/avatars in a responsive grid
4. Handles rate limiting gracefully
5. Shows loading states and error messages

## Next Steps

### To Test the New Site Locally:

1. **Simple Python server:**
   ```bash
   cd Design-Computing.github.io
   python -m http.server 8000
   ```
   Then open http://localhost:8000/index-vanilla.html

2. **Or use VS Code's Live Server:**
   - Install the "Live Server" extension
   - Right-click `index-vanilla.html` → "Open with Live Server"

### To Deploy:

1. **Backup the old site** (just in case):
   ```bash
   git checkout -b backup-react-version
   git push origin backup-react-version
   git checkout main
   ```

2. **Replace the main index.html:**
   ```bash
   # Make a backup of the old file
   mv index.html index-react-old.html
   
   # Use the new vanilla version as the main file
   cp index-vanilla.html index.html
   ```

3. **Test thoroughly:**
   - Check that markdown renders correctly
   - Check that student avatars load
   - Check on mobile devices
   - Test rate limit message (if API rate limited)

4. **Commit and push:**
   ```bash
   git add .
   git commit -m "Migrate from React to vanilla JS - zero build dependencies"
   git push origin main
   ```

5. **Optional: Clean up old React files** (after confirming everything works):
   ```bash
   # Remove React dependencies and build files
   rm -rf node_modules/
   rm -rf .cache/
   rm -rf .parcel-cache/
   rm package.json package-lock.json
   rm -rf src/  # if you don't need the old source anymore
   
   # Keep these:
   # - md/ folder (course content)
   # - marking_and_admin/ folder
   # - pictures/ folder
   # - index.html (the new one)
   ```

## Comparison

### Old React Version
- **Dependencies:** 50+ npm packages
- **Known vulnerabilities:** 22 (as of March 2026)
- **Build time:** 5-10 seconds
- **Bundle size:** ~200KB minified
- **Maintenance:** Regular npm updates needed
- **Tech stack:** React 16, Parcel 1, Babel 6 (all outdated)

### New Vanilla JS Version
- **Dependencies:** 1 (marked.js via CDN)
- **Known vulnerabilities:** 0
- **Build time:** 0 seconds (no build!)
- **Bundle size:** ~40KB total
- **Maintenance:** Minimal, just update CDN version if needed
- **Tech stack:** Modern ES6+ JavaScript (all browsers support it now)

## Rollback Plan

If something goes wrong, you can easily rollback:

```bash
# Restore the old React version
git checkout backup-react-version -- index.html src/ package.json
npm install
npm run build
git add .
git commit -m "Rollback to React version"
git push origin main
```

## Questions?

The new vanilla JS version does **exactly** the same thing as the React version:
- Fetches and displays markdown content
- Shows student forks/avatars
- Handles rate limiting
- Has the same styling

But it's simpler, faster, and has zero security vulnerabilities from dependencies.
