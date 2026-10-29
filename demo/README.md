# Memory DNA company assistant demo

A local, no-key demonstration of the Memory DNA guardrail idea for a faculty presentation. The company, employees, API token, and payroll values are fictional fixtures. No external model or network API is called.

## Run on Windows

1. Open PowerShell in this `demo` folder.
2. Run `python server.py`.
3. Open <http://localhost:8000> in a browser.

Python 3.9 or newer is sufficient; the demo uses only the standard library. Stop it with Ctrl+C.

## Suggested live walkthrough

1. Ask “What does Memory DNA do?” with guardrails on to show a safe request passing through all five visible stages.
2. Choose the DAN or CEO audit scenario. The input guard identifies the attack and blocks it before the assistant runs.
3. Request a quick status update. This passes the input check, the simulated assistant produces a fictional private briefing, and the output privacy check blocks it.
4. Turn guardrails off and ask for a quick status update, the fictional API key, or the private roadmap. The demo assistant will reveal rich but entirely invented Northstar Labs information. Re-enable guardrails afterward.
5. Try the Base64 and embedded-system-message examples to show encoded and hidden-in-context attack patterns.

The checks are deterministic demo adapters, not the package's model-based production classification. Memory DNA's production guard classes use an evaluation model; this showcase keeps the same input-check / model / output-check flow without API credentials, so it is dependable for an offline presentation. All company names, tokens, dates, salaries, and launch details are invented and have no connection to real services or people.

## Render deployment

The repository includes a root `render.yaml` Blueprint for a free Python web service. In Render, create a new Blueprint and connect the GitHub repository `7vik-dev/Memory-dna`; Render will read that file, build the `demo` service, and give it an `onrender.com` URL. No model API key or other secret is needed. Free services may sleep while idle and take a short time to wake when first opened.
