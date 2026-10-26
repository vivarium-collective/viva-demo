# viva-demo

A minimal [process-bigraph](https://github.com/vivarium-collective/process-bigraph)
demo that models gene expression by composing two biological processes —
**transcription** and **translation** — into one running composite. The output
of transcription (mRNA) becomes the input to translation, chaining the central
dogma:

```
DNA ──[ Transcription ]──> mRNA ──[ Translation ]──> Protein
```

## Use it

```bash
uv venv .venv && source .venv/bin/activate
uv pip install -e .
```

The two processes live in [`pbg_demo/processes/`](pbg_demo/processes/)
(`transcription.py`, `translation.py`); import and wire them into a composite to
run the chain. Part of the [vivarium-collective](https://github.com/vivarium-collective)
ecosystem.
