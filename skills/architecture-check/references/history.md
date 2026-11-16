# Reading git history

Commands for step 2. Run them from the repo root. Swap the path filters for the repo's source folders, and leave out lock files, generated code and docs.

## Hot spots

Files changed by the most commits since a date:

```bash
git log --since=<date> --name-only --format= -- <paths> | grep -v '^$' | sort | uniq -c | sort -rn | head -20
```

Start with six months. If that gives fewer than about 30 commits, use the whole history and say so.

## Change coupling

Pairs of files that change in the same commit. A pair that keeps changing together is one decision split across two places, or two lists kept in sync by hand:

```bash
git log --since=<date> --format=tformat:@@ --name-only -- <paths> \
  | awk '/^@@$/{for(i in f)for(j in f)if(i<j)c[i" "j]++; delete f; next} NF{f[$0]=1}
         END{for(i in f)for(j in f)if(i<j)c[i" "j]++; for(p in c)print c[p], p}' \
  | sort -rn | head -20
```

A pair counts when it changed together in at least a third of the commits that touched either file. A test file changing with the file it tests is expected: skip those pairs.

## Callers

To count the callers of a function for the deletion test, search for its name across the repo, then open each hit to check it really is a call. A search can miss dynamic calls (`getattr`, reflection, string dispatch), so report the count as "found by search".
