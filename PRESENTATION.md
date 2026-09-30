# NexGene v1.5.0 — presenter script

Use the deck `NexGene_v1_5_0_Presentation.pptx`. Target time: 8–10 minutes plus demo.

## Opening (slide 1)

NexGene is a personal living baseline. Not a doctor. Not a chatbot that invents labs.

Line to remember: *Private by default. Evidence before inference.*

## Problem (slide 2)

People already have fragments: sleep, energy, stress, the occasional lab PDF.
What they do not have is a system that keeps those fragments honest.

Do not attack other products by name. Attack the pattern: model-as-source-of-truth.

## Thesis (slide 3)

Structure first. Models later.
If the structured packet is wrong, the nicest sentence is still wrong.

## Architecture (slides 4–5)

Walk the five layers top to bottom.
Then stop on compartments: consumer / clinical / genomic.
The bridge is an opaque `subject_ref`. Dual authorization. Instant revoke.

If asked “is this HIPAA certified?”: No. This is a development foundation.

## What ships (slide 6)

Show only what exists: API, check-ins, weekly report, brief, live metadata search, learning worker, tests.

## Boundaries (slide 7)

Read the list slowly. This slide is how you keep trust.
If someone asks “so it can tell me if I have diabetes?”: No.

## Proof (slide 8)

21 tests passing. Isolated stores. Versioned 90-day learning window.
Repo: `github.com/faruoqu146-ctrl/NexGene_v1_5_0`

## Demo (slide 9)

```bash
docker compose up --build
# open http://localhost:8000
```

Script:

1. Register with a strong password.
2. Morning check-in: sleep 7.5, energy 8.
3. Open weekly report and intelligence brief.
4. Open clinical records — expect `not_authorized`.
5. Close on the sentence: observed facts stay upstream of AI.

## Close (slide 10)

Ask for the next controlled steps only:

- reviewed evidence corpus
- production secrets
- scheduled learning worker
- clinical-safety review before any escalation language goes live

Do not promise a hospital integration in this meeting.
