# worm

## file_process
### csv
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

## some codes
### The Crawler is in the directory worm, and the venv directory are package that you need.
