# Live Sessions

Live sessions by the instructors and TAs are recorded and uploaded to YouTube.

[[Image description: Here's alt text describing the image:

A vibrant, graphic illustration depicting various tools used in data science. The background is a pale yellow-beige.  The central focus is the text "TOOLS IN DATA SCIENCE" displayed prominently in a bold, sans-serif font. This text is within a dark rectangular box, positioned over a stylized laptop screen. The illustration is surrounded by a diverse collection of colorful icons representing data visualization charts, graphs, programming elements, and other data-related symbols, all rendered in a flat, geometric style using a palette of blues, reds, oranges, yellows, and blacks. The overall style is modern and playful, conveying the dynamic nature of the data science field.]](https://www.youtube.com/playlist?list=PL_h5u1jMeBCl1BquBhgunA4t08XAxsA-C)

These were downloaded using [yt-dlp](https://github.com/yt-dlp/yt-dlp). The options compress the audio optimized for speech.

```bash
yt-dlp --extract-audio --audio-format opus --embed-thumbnail --postprocessor-args \
  "-c:a libopus -b:a 12k -ac 1 -application voip -vbr off -ar 8000 -cutoff 4000 -frame_duration 60 -compression_level 10" \
  $YOUTUBE_URL
```

They were then transcribed by Gemini 1.5 Flash 002 (currently the best model from a price-quality perspective for audio transcription).

System prompt:

```
You are an expert transcriber of data science audio tutorials
```

User prompt:

```
Transcribe this audio tutorial about Tools in Data Science (TDS) as an FAQ.
Summarize the student questions faithfully.
Summarize the answers succinctly, without missing information, in a conversational style.
Avoid repeating questions, consolidating similar ones.
Prefer "You" and "I" instead of "student" and "instructor".
For example:

**Q1: [Concisely framed question]**

**A1:** [Succinct answer]
```
