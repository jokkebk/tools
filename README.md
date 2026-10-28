# Tools Index

## Alphabetical Index

* [aquarium](aquarium.html)
* [blackjack_trainer](blackjack_trainer.html)
* [colorfill](colorfill.html)
* [crt_simulator](crt_simulator.html)
* [dustline](dustline.html)
* [find_fraction](find_fraction.html)
* [firefighter](firefighter.html)
* [jokeripokeri_advisor](jokeripokeri_advisor.html)
* [jokeripokeri_trainer](jokeripokeri_trainer.html)
* [launchpad_chess](launchpad_chess.html)
* [launchpad_test](launchpad_test.html)
* [monsterbrush](monsterbrush.html)
* [pianotrainer](pianotrainer.html)
* [rushhour](rushhour.html)
* [samefile](samefile.html)
* [triangles](triangles.html)
* [wordle](wordle.html)
* [wordle-ocr](wordle-ocr.html)
* [zipview](zipview.html)

## Tools

### [monsterbrush](monsterbrush.html)

Brush six friendly monsters' teeth, including Pumpkin, Pip the big-eared bat, and Boo the floating mint ghost. Thirty-second sessions celebrate when 99% of the tooth dirt is removed, with a closer view on phones and clean smiles remembered on this device for six hours. Tap the moon for a gentle good-night view where every monster has clean teeth and tapping a friend makes it wave.

> last updated: 2026-10-28 23:40:06
> Add Pip the bat and Boo the ghost to Monsterbrush
>
> [view commit](https://github.com/jokkebk/tools/commit/2ab1d749600f39aa31a24abad20da6ac96cc0bb1)

### [aquarium](aquarium.html)

A WebGL2 planted aquarium that runs as a real simulation rather than a loop: the caustics on the sand are computed by refracting a dense grid of light through the same wave field that shapes the visible surface and splatting it onto the substrate, so the dancing net is physically tied to the ripples overhead and is energy-conserving by measurement. Five species of procedurally modelled fish swim as boids with per-species schooling, depth preference and body-wave animation, casting shadow-mapped silhouettes that cut through volumetric light shafts, while plants sway in a shared current field and an air stone sends refractive bubbles to the surface. Tap or click the water to drop food and watch the shoal converge; twenty sliders control fish, planting, lamp colour and angle, water clarity, caustics, shafts, surface ripple, current, camera and render scale, and everything is remembered between visits.

> last updated: 2026-08-23 16:07:58
> Add WebGL2 aquarium simulation
> 
> Photoreal planted tank rendered in eight passes. Caustics are a forward
> photon splat: a grid of surface samples is refracted onto the substrate
> with additive blending, so overlapping ray branches build the bright
> filaments an inverse Jacobian cannot see. The map's mean is read back and
> inverted each time the ripple slider moves, keeping it energy-conserving.
> 
> The visible surface, caustic map and volumetric shafts all evaluate one
> shared wave field, tileable by construction. Adds a shadow-mapped light
> volume, a mirrored render for total internal reflection with Snell's
> window, per-channel water extinction, and boids-driven procedural fish.
> 
> Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
>
> [view commit](https://github.com/jokkebk/tools/commit/ad8ac83c31f8e4b92884f9bc483168ca372b96ea)

### [launchpad_chess](launchpad_chess.html)

Play full chess on a Novation Launchpad Mini MK3 over Web MIDI: each pad is a square, white pieces glow green and black pieces purple, and tapping a piece then a destination makes the move with orange valid-move and red capture highlights. The on-screen board mirrors the grid with move-history navigation, captured-piece tallies, and PGN saving or drag-and-drop loading.

> last updated: 2026-08-10 12:21:43
> Add Launchpad Chess tool
>
> [view commit](https://github.com/jokkebk/tools/commit/bb6aa6af09e6e9ae658dc88956d128e22b82e25a)

### [zipview](zipview.html)

Drop one or more ZIP files, or open a folder, and this browser-only ZIP Image Viewer indexes archives locally without uploading anything. It lazily decompresses the active archive with fflate, builds responsive thumbnail previews only as they scroll into view, and keeps full-size image blobs limited to the current viewer image. The fullscreen viewer supports fit and clicked-position 1:1 zoom, pointer-lock panning, wheel or keyboard image navigation, and explicit archive switching for folders with multiple ZIPs.

> last updated: 2026-08-01 00:25:53
> Improve zipview zoom for small images
>
> [view commit](https://github.com/jokkebk/tools/commit/f328d1960103111ecf0f74b994beb9df33636a12)

### [dustline](dustline.html)

Dustline is a sideways-scrolling physics racing game with procedurally generated courses, three distinct vehicles (motocross bike, monster truck, rally car) and realistic spring-damper suspension simulated on a Verlet particle chassis. Regenerate or share seeded courses from the start screen, then race the clock against your best ghost or pass the keyboard in 2–4 player party mode. Surfaces (asphalt, dirt, gravel) change grip, water hazards can be jumped or hydroplaned at speed, and nitro recharges through airtime — land clean to keep your momentum.

> last updated: 2026-07-14 22:41:56
> Dustline: fix nitro cutting out on bumpy ground, buff truck climbing
> 
> Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
>
> [view commit](https://github.com/jokkebk/tools/commit/eec80d8abbb00d2ba0724423bef5363abb6ed2c3)

### [colorfill](colorfill.html)

Colorfill is a small, touch-friendly image coloring app. Upload or paste a coloring page, tap regions to flood fill them, pinch to zoom and pan on an iPad, then download the finished PNG.

> last updated: 2026-07-13 22:47:53
> Fix Colorfill iPad layout
>
> [view commit](https://github.com/jokkebk/tools/commit/45317c08a8e430f8f9e8b5afecbe6a0825af8cf7)

### [wordle-ocr](wordle-ocr.html)

Wordle Screenshot OCR reads a pasted or uploaded Wordle screenshot with Tesseract.js, then shows the recognized letters in an editable tile grid that preserves gray, yellow, and green colors.  Correct letters inline with the keyboard, tap tiles to cycle colors, and optionally inspect the cleaned row/tile images sent to OCR.  It intentionally avoids dictionary matching while expanding known-letter location patterns into the first 100 brute-force fills.

> last updated: 2026-06-06 08:28:00
> Add OCR debug viewer and row-level recognition
>
> [view commit](https://github.com/jokkebk/tools/commit/05d632efc000767d000f1080bd0f656aa631f552)

### [samefile](samefile.html)

Samefile is a browser-only duplicate finder that groups files by size and hashes the first N bytes using SHA-256. It scans a user-selected folder via the File System Access API and reports matches as `size hash path` lines. Optional include/exclude globs and a minimum size filter help narrow the search.

> last updated: 2026-01-27 13:30:01
> Add filters and docs for samefile tool
>
> [view commit](https://github.com/jokkebk/tools/commit/2b6a16d11e95da254dc2d5d0993f0cec56e06634)

### [triangles](triangles.html)

Approximate any image using semi-transparent triangles through evolutionary algorithms. Upload your own image or try classic artworks like Mona Lisa and Starry Night. Watch the evolution in real-time and export high-resolution PNGs or JSON triangle data.

> last updated: 2026-01-08 13:33:30
> Add triangle evolution image approximator
> 
> Genetic algorithm tool that approximates images using semi-transparent
> triangles. Features sample images from Wikimedia Commons, live progress
> tracking, stop button, high-res PNG export, and JSON export.
> 
> Also clarifies in CLAUDE.md that sidecar .md files should be 2-3 sentences.
> 
> 🤖 Generated with [Claude Code](https://claude.com/claude-code)
> 
> Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
>
> [view commit](https://github.com/jokkebk/tools/commit/53648a544444ea98f3748a39b8b761ec880e54ff)

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

