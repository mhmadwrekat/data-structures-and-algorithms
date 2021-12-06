# Trace

---
## ***Sample list*** = [38 ,27 ,43 ,3 ,9 ,82 ,10]

## Phase 1 :
- list = [38 ,27 ,43 ,3 ,9 ,82 ,10]
- Split the list into two halfes :
- left = [38 ,27 ,43 ,3]
- right = [9 ,82 ,10]

## Phase 2 :
- left-list = [38 ,27 ,43 ,3]
- Split the first half (left) list into two halfes :
- left-left = [38, 27]
- right-left = [43, 3]

## Phase 3 :
- left-left-list = [38 ,27]
- Split this list into left = [38] and right = [27] and sort and merge them -> [27 ,38 ]

## Phase 4 :
- Merge the left-left-list after we sorted it and right-left list in a way that they stay sorted :
- left-list = [3 ,27 ,38 ,43]

## Phase 5 :
- right-list = [9 ,82 ,10 ]
- Split the second half list into two halfes :
- left-right = [9 ,82 ]
- right-right = [10]

## Phase 6 :
- left-right-list = [9 ,82 ]
- Split this list into left = [9] and right = [82] and sort and merge them -> [9 ,82 ]

## Phase 7 :
- Merge the left-right-list after we sorted it and right-right list in a way that they stay sorted :
- right-list = [9 ,10 ,82 ]

## Phase 8 :
- Sort and merge the final two halfes :
- the list after it sorted = [3 ,9 ,10 ,27 ,38 ,82]

