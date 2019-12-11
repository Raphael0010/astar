# A * PathFinder

## Definition

0 = Wall  
X >= 1 is the cost 

It's based on the cost of the path and an estimate of the cost required to extend the path all the way to the goal.

```bash
 array = [[1, 0, 1, 1, 1],
         [1, 1, 1, 5, 1],
         [1, 0, 0, 1, 1],
         [1, 0, 1, 3, 2],
         [1, 0, 1, 1, 1]]
```
=

```
-> 4,4 -> 3,4 -> 2,4 -> 1,4 
-> 0,4 -> 0,3 -> 0,2 -> 1,2
-> 1,1 -> 1,0 -> 2,0 -> 3,0 
```

=


<img src="https://github.com/Raphael0010/astar/blob/master/img/path.png?raw=true" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" width="250" height="250" />

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

### Thanks to [@yovanoc](https://github.com/yovanoc)

## License
[MIT](https://choosealicense.com/licenses/mit/)
