# cspy_snippets

| Problem | Type | Name |
| ------------ | ------------ | ------------ |
| Understanding Arrays and Hashmaps | notes | [arrays_and_dictionaries.ipnyb](https://github.com/CodyCardinal/csp_snippets/blob/main/arrays_and_dictionaries.ipnyb)|
| [CS50 Nutition Problem](https://cs50.harvard.edu/python/2022/psets/2/nutrition/) | solution | [nutrition.py](https://github.com/CodyCardinal/csp_snippets/blob/main/nutrition.py)|
| An Array of Floats Exercise, from [Fluent Python,2nd Ed](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/) | excercise | [array_of_floats.py](https://github.com/CodyCardinal/csp_snippets/blob/main/array_of_floats.py) |
| Testing Arrays vs Dictionaries | exercise | [hashmap_vs_arraylist.py](https://github.com/CodyCardinal/csp_snippets/blob/main/hashmap_vs_arraylist.py) |

## Results of Hasmap vs Arraylist

Create Test
- Array Length 10,000,000 @ `1.07 s` ± 6.18 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
- Dict Length 10,000,000 @ `898 ms` ± 30.3 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

Lookup Test
- Array @ `39.2 ns` ± 0.0147 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
- Dict @ `30 ns` ± 0.837 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

Insert Test
- Array @ `104 ns` ± 7.97 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
- Dict @ `54.3 ns` ± 0.0261 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

Removal Test
- Array @ `142 ms` ± 1.67 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
- Dict @ `39.1 ns` ± 0.824 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
