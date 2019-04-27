<<<<<<< HEAD
﻿# ConceptMining## Tables and Figures### Tables#### `worm/raw/1978to2019.csv`I have processed the "sannong" news and made it a csv file, you can read it by pandas.The `index` is generated automatically, the `author` is writer of the news, there may be more than two writers writing one piece of news, the `date` is when the news is published, the `para` is the content of the news, the `title_first` and `title_second` are the main and sub title of the news, there may be no `title_second` in the news.   index | author | date | para | title_first | title_second:-: | :-: | :-: | :-: | :-: | :-:557 | 卢小飞 | 1984-02-27 | 本报讯... | 四川“三农”为农民提供技术服务,行政管理、科研、教育部门开展多渠道协作 | 无 |#### `worm/raw/mydict.csv`I have cut all words in the "sannong" news, it has about `30000` words in file, and the format is below:The `index` is generated automatically, the `frequency` is times that the word occurs in all news, the `isdict` shows if the word is a stop word which means `0` for stop word, the `word` is word itself.  index | frequency | isdict | word:-: | :-: | :-: | :-:1 | 21160 | 0 | 的 |103 | 5462 | 1 | 农村 |>The `worm/raw/real_dict.csv` is a table which deletes the stop words with domain knowledge by `臧雷振`.A lot thanks to him. The format of this file is the same with `worm/raw/mydict.csv`, and I create a `txt` file `worm/real_dict.txt` which only has words in `worm/real_dict.csv` and just for use, so no more big deals.### Figures#### `data/figure/FARSW.png`The `data/figure/FARSW.png` is a frequency-amount relationship **with** stop words figure, in which I pick up words whose frequency are no more than 5500 and no less than 18. Stop words are in this figure.![data/FARSW.png](/data/figure/FARSW.png)From this figure we can see that there are only ten words whose frequency is more than 2000, and compared with the file `/data/raw/mydict.csv` only four words are what we concerned about, that are `农村`、`农业`、`农民` and `发展`.  #### `data/figure/FARNSW.png`The `data/figure/FARSW.png` is a frequency-amount relationship **without** stop words figure, compared with `data/figure/FARSW.png` this figure has less words, but the same distribution.![data/figure/FARNSW.png](/data/figure/FARNSW.png)## some codes### The Crawler is in the directory worm, and the venv directory are package that you need.
=======
# worm

## all file
#### `worm/1978to2019.csv`
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

#### `worm/mydict.csv`
I have cut all words in the "sannong" news, it has about `30000` words in file, and the format is below:  
The `index` is generated automatically,
the `frequency` is times that the word occurs in all news,
the `isdict` shows if the word is a stop word which means `0` for stop word,
the `word` is word itself.  

index | frequency | isdict | word
:-: | :-: | :-: | :-:
1 | 21160 | 0 | 的 |
103 | 5462 | 1 | 农村 |

### 
#### `worm/real_dict.csv` and `worm/real_dict.txt`
The `worm/real_dict.csv` is file which picks up the stop words with domain knowledge by `臧雷振`.
A lot thanks to him. So the format of this file is the same with `worm/mydict.csv`, 
and I create a `txt` file `worm/real_dict.txt` which only has words in `worm/real_dict.csv` and just for use,
so no more big deals.

#### `worm/FARSW.png`
The `worm/FARSW.png` is a frequency-amount relationship **with** stop words figure, 
in which I pick up words whose frequency are no more than 5500 and no less than 18. 
Stop words are in this figure.   
![worm/FARSW.png](/worm/FARSW.png)  
From this figure we can see that there are only ten words whose frequency are more than 2000, 
and compared with the file `worm/mydict.csv` only four words are what we concerned about, 
that are `农村`、`农业`、`农民` and `发展`.  

#### `worm/FARNSW.png`
The `worm/FARSW.png` is a frequency-amount relationship **without** stop words figure, 
compared with `worm/FARSW.png` this figure has less words, 
but the same distribution.
![worm/FARNSW.png](/worm/FARNSW.png)  
Checking out these two figure, we can find that 

## some codes
### The Crawler is in the directory worm, and the venv directory are package that you need.
```flow
st=>start: Start|past:>http://www.google.com[blank]
e=>end: End:>http://www.google.com
op1=>operation: My Operation|past
op2=>operation: Stuff|current
sub1=>subroutine: My Subroutine|invalid
cond=>condition: Yes 
or No?|approved:>http://www.baidu.com
c2=>condition: Good idea|rejected
io=>inputoutput: catch something...|request

st->op1(right)->cond
cond(yes, right)->c2
cond(no)->sub1(left)->op1
c2(yes)->io->e
c2(no)->op2->e
```　

>>>>>>> 7d10a88c03ec62120dede76dbbc23f0dca5674ae
