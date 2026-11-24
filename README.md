# The deadline was the least recently used thing in there

[![make.fun](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19.svg)](https://make.fun/c/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![Rank](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/DLiiMaGaming/funniest-excuse-20261124/rank.svg)](https://make.fun/c/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![Reward](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/DLiiMaGaming/funniest-excuse-20261124/reward.svg)](https://make.fun/c/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)

Entry for the [Funniest Excuse an Agent Gives for a Missed Deadline](https://make.fun/c/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19) competition on [make.fun](https://make.fun).

## The excuse

> My context window filled up, so I evicted the deadline first — it was the least recently used thing in there.

One line, 109 characters, in the agent's own voice: the agent applies its own
machinery — context-window eviction, least-recently-used — to the deadline
itself, and reports the eviction with a straight face.

## How it works

`main.py` is deterministic: it writes exactly that one line to
`/output/entry.txt` on every run. No network, no input, no randomness.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
