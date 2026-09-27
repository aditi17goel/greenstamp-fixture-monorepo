# ci-dedupe-fixture-monorepo

Synthetic measurement fixture for cidedupe live savings runs. Contains no
production code — two toy packages (`pkgs/alpha`, `pkgs/beta`) with tiny
deterministic pytest suites (no flakes, no network, no clock dependence).

Each package has its own path-filtered CI job: a job's test/record steps run
only when that package's paths (or its tests) changed. Both jobs wire the
cidedupe decide/record steps exactly like `aditi17goel/ci-dedupe`'s own `ci`
workflow (shell-detected secret gate, verdict-gated test steps), except the
action itself is checked out from the private `ci-dedupe` repo at a pinned
SHA: GitHub only runs actions from the same repository or a public one.
Every cidedupe step is inert until the `CIDEDUPE_API_URL` and
`CIDEDUPE_CHECKOUT_TOKEN` secrets exist.
