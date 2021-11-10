# A function that stretches subtitles by a given factor - Python
## Introduction
A function that:
* reads `.srt` subtitle file 
* multiplies each individual subtitle by a specified factor e.g. 1.04
* saves to a new `.srt` subtitle file

## Practical use
When the speed or duration of a film or video is changed the subtitles have to be adjusted. This python function accomplishes it automatically by simply pointing at the `.srt` file and specifying the factor of the speed change.

I ran into this task when I needed to convert the film from 25 fps to 24 fps by increasing the speed/duration of the film by 25/24 or 1.041667.

## Input
Standard `.srt` subtitle file in the following format:

```
1
00:00:03,400 --> 00:00:06,177
In this lesson, we're going to
be talking about finance. And

2
00:00:06,177 --> 00:00:10,009
one of the most important aspects
of finance is interest.

...

23
00:01:46,860 --> 00:01:49,970
find an institution that will pay
me a higher interest rate.
```
## Output
Standard `.srt` subtitle file that can be imported in any video editing software or straight to Vimeo or YouTube.

In the example below subtitles are stretched by the factor of 1.041667.

```
1
00:00:03,541 --> 00:00:06,434
In this lesson, we're going to
be talking about finance. And

2
00:00:06,434 --> 00:00:10,426
one of the most important aspects
of finance is interest.

...

23
00:01:51,312 --> 00:01:54,552
find an institution that will pay
me a higher interest rate.
```

## Importing to video editor FinalCut Pro
Launch **FinalCut Pro** and select File -> Import -> Captions, then select `.srt` file to import subtitles into Video Editing software.
