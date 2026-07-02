# pbg-demo

A demo project built on [process-bigraph](https://github.com/vivarium-collective/process-bigraph) that
models gene expression by composing two biological processes — **transcription** and **translation** —
into a single running composite. The output of transcription (mRNA) becomes the input to translation,
chaining the central dogma:

```
DNA ──[ Transcription ]──> mRNA ──[ Translation ]──> Protein
```