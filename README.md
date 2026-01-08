# Tools Index

## Alphabetical Index

* [blackjack_trainer](blackjack_trainer.html)
* [christmas-screensaver-opus45](christmas-screensaver-opus45.html)
* [crt_simulator](crt_simulator.html)
* [find_fraction](find_fraction.html)
* [firefighter](firefighter.html)
* [jokeripokeri_advisor](jokeripokeri_advisor.html)
* [jokeripokeri_trainer](jokeripokeri_trainer.html)
* [launchpad_test](launchpad_test.html)
* [pianotrainer](pianotrainer.html)
* [rushhour](rushhour.html)
* [wordle](wordle.html)
* [zipview-gpt52pro](zipview-gpt52pro.html)
* [zipview-opus45](zipview-opus45.html)

## Tools

### [crt_simulator](crt_simulator.html)

CRT display simulator that renders images through an authentic phosphor grain pattern with RGB shadow mask, scanlines, and animated luminance noise. Supports drag-and-drop, paste, or file browse for image input, with three selectable resolution modes: SPECTRUM (256x192), CGA (320x200), and VGA (640x480). Resolution auto-selects based on viewport size but can be cycled manually via the corner toggle.

> last updated: 2026-01-08 11:25:52
> Add CRT display simulator with phosphor grain rendering
> 
> Simulates classic CRT displays with authentic RGB shadow mask pattern,
> scanlines, and luminance noise. Supports three resolution modes
> (SPECTRUM, CGA, VGA) with auto-selection based on viewport size.
> 
> 🤖 Generated with [Claude Code](https://claude.com/claude-code)
> 
> Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
>
> [view commit](https://github.com/jokkebk/tools/commit/e6d08e7c3ce55d81adb294cf6978163ade4664bb)

### [launchpad_test](launchpad_test.html)

Launchpad Mini Toolkit connects to the hardware via Web MIDI and provides three modes—Debug, Blob Tap, and Snake—for exercising or experimenting with the grid.  The page mirrors pad activity on a canvas, streams MIDI log messages, and even lets you spawn animated blobs or run a playable snake game while syncing the Launchpad lights.  Mode controls and hints switch dynamically so you can toggle behaviors without leaving the browser session.

> last updated: 2026-01-04 09:28:22
> Novation Launchpad Mk3 test suite and snake/blob games
>
> [view commit](https://github.com/jokkebk/tools/commit/b82b9593e6e7b19fab147594dd2df49e5cd48965)

### [jokeripokeri_advisor](jokeripokeri_advisor.html)

Select any five cards (including the Joker) from the grid, and the advisor computes the top EV selections for which cards to keep or discard.  The interface also accepts an optional Gemini API key so you can upload or photograph a hand and let the AI transcribe the five cards automatically.  Results highlight the best three plays, show each card as part of the original hand, and score them using the in-page Jokeripokeri payoff logic.

> last updated: 2025-12-29 17:30:12
> Jokeripokeri advisor tool with image upload capability w. Google API key
>
> [view commit](https://github.com/jokkebk/tools/commit/2279684e6b2f281acd34b567f45db692334c544b)

### [jokeripokeri_trainer](jokeripokeri_trainer.html)

Jokeripokeri Trainer deals a hand of five cards, lets you tap the ones you want to keep, and then shows message feedback once you press the deal button to rerun the next hand.  The sidebar keeps running totals for games, winnings, average payout, and a separate optimistic strategy tracker so you can compare your selections to the theoretical expectation.  An expandable table below documents the optimal combinatorics while the CSS-only cards keep everything sharp-looking on both desktop and mobile viewports.

> last updated: 2025-12-29 15:29:23
> Jokeripokeri optimal selection trainer redone to SPA w. Opus 4.5
>
> [view commit](https://github.com/jokkebk/tools/commit/964330e160f52fe70b6f2a703a2804e2f5838a88)

### [rushhour](rushhour.html)

Rush Hour Solver renders the classic 6×6 grid with draggable cars and an exit marker so you can set up puzzles manually or load one of the built-in sample configurations.  The Vue-powered UI lets you step through moves, see legal drops, and use the solver logic to compute a sequence that frees the red target car.  Controls include reset/sample buttons, move history, and visual feedback for the board, all inside a single responsive page.

> last updated: 2025-12-28 20:46:40
> Rush Hour solver, UI pimped with Claude Opus 4.5
>
> [view commit](https://github.com/jokkebk/tools/commit/4f8ad3d61ed235494353d2456270ac57da68e0b3)

### [find_fraction](find_fraction.html)

Type a decimal number, pick how many digits of accuracy you need, and the page shows the nearest rational approximations up to that precision.  It is a lightweight converter that keeps refining fractions as you increase the target decimal places and displays them in a monospaced answer box.  No backend is involved—everything is done in the browser using the tiny script bundled in the HTML.

> last updated: 2025-12-28 20:09:07
> Find the fraction corresponding to a decimal number
>
> [view commit](https://github.com/jokkebk/tools/commit/a7af8d2895c54886b5efa5ebfd0cf9a6ca8dcadf)

### [wordle](wordle.html)

Wordle Solver accepts a compact notation for past guesses (dots for misses, lowercase for present, uppercase for exact) and filters the built-in word list in real time.  The Vue frontend shows each submitted guess with colored tiles, keeps a history list, and highlights the remaining candidate words with rankings.  Instructional help text and responsive styling make this a quick browser helper for staying organized while you puzzle through your current game.

> last updated: 2025-12-28 19:53:38
> Wordle letter order brute forcer for the lazy
>
> [view commit](https://github.com/jokkebk/tools/commit/351f0b016a72f78fb39b18e0d89fe9dc729f741d)

### [blackjack_trainer](blackjack_trainer.html)

This Blackjack Basic Strategy Trainer deals a player and dealer hand, then asks you to pick hit/stand/double/split while highlighting the right answer.  The UI renders cards with gradients, keeps statistics for each action (plus a total row), and shows a verdict message after every decision.  Checkbox options and a toggleable strategy chart keep the reference info nearby so you can practice without leaving the single page.

> last updated: 2025-12-28 13:20:23
> Blackjack trainer for basic strategy
>
> [view commit](https://github.com/jokkebk/tools/commit/868a96d54419da1a8e6a440f382b27c3714c87ab)

### [pianotrainer](pianotrainer.html)

Piano Trainer draws a clean staff and piano keyboard in SVG, then prompts you with notes to emulate using left or right hand, selectable via the floating controls.  Touch or click anywhere on the piano area and the script highlights the notes on the staff, plays the target, and advances when you hit each of eight notes correctly.  The experience is optimized for touch devices with a fixed control bar, so you can practice bass (left) and treble (right) ranges purely in the browser.

> last updated: 2025-12-28 13:03:03
> Left/right hand piano trainer
>
> [view commit](https://github.com/jokkebk/tools/commit/594cd68236c86c08329fa290929963bf4a0fc273)

### [firefighter](firefighter.html)

Firefighter: Gingerbread Defense is a canvas-based action game where you aim a cannoniac water stream to quench spreading fires before they overwhelm the gingerbread village.  Difficulty presets change how fast fires grow, how much water/health you have, and how aggressive shooting stars or fire spreads become, while on-screen gauges keep you aware of health, water, angle, and power.  The UI includes start/game-over overlays, controls help, and feedback so you can adjust angle/power, keep firing, and survive long enough for bonus points.

> last updated: 2025-12-27 00:58:37
> Add PWA support for fullscreen mobile experience
> 
> - Add web app manifest for "Add to Home Screen" functionality
> - Add PWA meta tags for iOS and Android
> - Use dynamic viewport height (dvh) to account for browser UI
> - Add safe area insets for notched devices
> - Request fullscreen when game starts
> 
> 🤖 Generated with [Claude Code](https://claude.com/claude-code)
> 
> Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
>
> [view commit](https://github.com/jokkebk/tools/commit/14bccc1cf23eba2bef3a41e92d23e1031a87507a)

### [christmas-screensaver-opus45](christmas-screensaver-opus45.html)

Nordic Christmas Night layers WebGL aurora ribbons, a scene canvas, and a snow canvas to render a calm holiday screensaver entirely in the browser.  The aurora shader demos simplex noise, fbm, and color blending to create flowing bands, while other layers add the silhouette scene, snow effects, and faint help hints for interaction.  Everything is fullscreen, cursor-free, and tuned for atmosphere so you get a looping northern lights display without any manual input.

> last updated: 2025-12-18 09:03:18
> Claude Opus 4.5 Christmas screensaver two-prompt test
>
> [view commit](https://github.com/jokkebk/tools/commit/1a2f530d2f4d4ee228f74bfa4f8678b86e0ef96c)

### [zipview-opus45](zipview-opus45.html)

Drop a ZIP file that contains JPEG/PNG/GIF/WebP images anywhere on the page and the client decompresses it with fflate, filters to supported extensions, and populates a responsive thumbnail grid.  Each thumbnail lazily loads a blob URL, and clicking one opens a fullscreen viewer that supports fit and pointer-locked 1:1 navigation plus keyboard or wheel-based image stepping.  The app keeps your ZIP processing local, shows an extractor spinner while indexing contents, and overlays contextual tips for zooming and panning.

> last updated: 2025-12-16 21:43:39
> Claude Opus 4.5 and ChatGPT 5.2 Pro created image viewers. Polished by Claude Code w. Sonnet.
>
> [view commit](https://github.com/jokkebk/tools/commit/18535cf925056e4946444e777e16524f2ffa7170)

### [zipview-gpt52pro](zipview-gpt52pro.html)

This ZIP Image Viewer decompresses archives entirely in the browser with fflate, lazily creating thumbnails as it filters supported image extensions, and it exposes a sticky top bar once content loads.  Grid tiles overlay names, file sizes, and thumb placeholders while a fullscreen viewer supports fit/1:1 toggling, pointer-lock panning, and keyboard navigation between images.  Drop hints, drag-over styling, and a reset button keep interactions discoverable, so it behaves like a polished photo review utility without ever uploading your files.

> last updated: 2025-12-16 21:43:39
> Claude Opus 4.5 and ChatGPT 5.2 Pro created image viewers. Polished by Claude Code w. Sonnet.
>
> [view commit](https://github.com/jokkebk/tools/commit/18535cf925056e4946444e777e16524f2ffa7170)

