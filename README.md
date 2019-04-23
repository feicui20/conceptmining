# worm

## csv file
### `worm/1978to2019.csv`
I have processed the "sannong" news and made it a csv file, you can read it by pandas.  
The `index` is generated automatically, 
the `author` is writer of the news, 
there may be more than two writers writing one piece of news, 
the `date` is when the news is published, 
the `para` is the content of the nes, 
the `title_first` and `title_second` are the main and sub title of the news, 
there may be no `title_second` in the news.   

index | author | date | para | title_first | title_second
:-: | :-: | :-: | :-: | :-: | :-:
557 | 卢小飞 | 1984-02-27 | 本报讯... | 四川“三农”为农民提供技术服务,行政管理、科研、教育部门开展多渠道协作 | 无 |

### `worm/mydict.csv`
I have cut all words in the "sannong" news, it has about `30000` words in file, and the format is below:  
The `index` is generated automatically,
the `frequency` is times that the word occurs in all news,
the `isdict` shows if the word is a stop word which means `0` for stop word,
the `word` is word itself.  

index | frequency | isdict | word
:-: | :-: | :-: | :-:
1 | 21160 | 0 | 的 |
103 | 5462 | 1 | 农村 |

## some codes
### The Crawler is in the directory worm, and the venv directory are package that you need.
