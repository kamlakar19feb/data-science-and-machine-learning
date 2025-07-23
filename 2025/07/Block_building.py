# Enter your code here. Read input from STDIN. Print output to STDOUT
def solve():
    n=int(input())
    blocks=list(map(int,input().split()))
    left_ptr=0
    right_ptr=n-1
    last_block_on_pile = float('inf')
    possible= True
    while left_ptr<=right_ptr:
        left_block = blocks[left_ptr]
        right_block = blocks[right_ptr]
        if left_block>=right_block:
            if left_block<=last_block_on_pile:
                last_block_on_pile=left_block
                left_ptr+=1
            else:
                possible=False
                break
        else:
            if right_block<=last_block_on_pile:
                last_block_on_pile=right_block
                right_ptr-=1
            else:
                possible=False
                break
    if possible:
        print("Yes")
    else:
        print("No")
T=int(input())
for _ in range(T):
    solve()