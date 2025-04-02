# 数据结构及应用

## 数组

### 数组的基本算法设计

#### **1.移除元素（双指针）**

``` python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums) ):
            if nums[fast] != val:
                nums[slow] = nums[fast]
            
                slow += 1
        return slow

```

``` C++
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int slow = 0 ;
        for(int fast = 0 ; fast < nums.size();fast ++)
        {
            if (nums[fast] != val)
            {
                nums[slow] = nums[fast];
                slow ++ ;
            }
        }
        return slow;
    }
};
```

#### 2.移动零（多方法）

``` python
# 双指针法
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        # 第一个0之前的元素，并没有交换，属于是自己给自己赋值
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow],nums[fast] = nums[fast],nums[slow]
                slow += 1
                

# 入栈法
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        stack_size = 0
        for i , x in enumerate(nums):
            # x非0时
            if x :
                nums[stack_size] = x
                stack_size += 1
        for i in range(stack_size , len(nums)):
            nums[i] = 0
        
```

``` C++
// 双指针
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int pre = 0;
        for (int &x:nums)
        {
            if (x)
            {
                swap(x,nums[pre]);
                pre ++;
            }
        }
    }
};

//入栈
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int stack_size = 0;
        for (int &x : nums)
        {
            if(x)
            {   
                nums[stack_size] = x;
                stack_size ++;
            }
        }
        // for(int res = stack_size ; res < nums.size() ; ++res)
        // {
        //     nums[res]  = 0;
        // }
        fill(nums.begin() + stack_size , nums.end() , 0);
    }
};
```

#### 3.对数组执行操作

``` python
# 双指针：同上移动零
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        j = 0
        for i in range(len(nums)):
            if i+1 < len(nums) and nums[i] == nums[i+1]  :
                nums[i] *= 2
                nums[i+1] = 0
            if nums[i] != 0:
                nums[j],nums[i] = nums[i],nums[j]
                j += 1
        # 下面的循环是多余的操作
        for i in range(j,len(nums)):
            nums[i] = 0
        return nums
```

``` C++
class Solution {
public:
    vector<int> applyOperations(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0 , j = 0; i < n ; ++i)
        {
            if( i + 1 < n && nums[i] == nums[i + 1] )
            {
                nums[i] *= 2;
                nums[i + 1] = 0;
            }
            if(nums[i] != 0)
            {
                swap(nums[j],nums[i]);
                j++;
            }
        }
        return nums;
    }
};
```

#### 4.颜色分类（双指针交换）

``` 
```

#### 5.轮转数组

``` python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k > 长度时，取余
        k = k % len(nums)
        def reverse(i:int,j:int) -> None:
            while i < j:
                nums[i] , nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        reverse(0,len(nums)-1)
        reverse(0,k-1)
        reverse(k,len(nums)-1)
```

``` C++
class Solution {
public:
    void reverse(vector<int>& nums,int i ,int j)
        {
            while (i < j)
            {
                swap(nums[i++],nums[j--]);
                
            }
        }
    void rotate(vector<int>& nums, int k) {
        k %= nums.size();
        
        reverse(nums,0,nums.size()-1);
        reverse(nums,0,k-1);
        reverse(nums,k,nums.size()-1);
    }
};

//另一种写法
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        //lambda（匿名函数）写法
        auto reverse = [&](int i, int j) {
            while (i < j) {
                swap(nums[i++], nums[j--]);
            }
        };

        int n = nums.size();
        k %= n; // 轮转 k 次等于轮转 k % n 次
        reverse(0, n - 1);
        reverse(0, k - 1);
        reverse(k, n - 1);
    }
};


```

### 有序数组的算法设计

#### 删除有序数组中的重复项Ⅰ（双指针）

``` python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # slow从1开始的原因是：nums[0]一定会被保留
        slow = 1
        for fast in range(1,len(nums)):
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast] 
                slow += 1
        return slow  
```

C++思路同双指针，没啥变化，就不写了

#### 删除有序数组中的重复项II

``` python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        stack_size = 2
        for i in range(2,len(nums)):
            # stack_size 指向要入栈的位置，所以栈顶下方那个元素是nums[stack_size - 2]
            if nums[stack_size - 2] != nums[i]:
                nums[stack_size] = nums[i] # 入栈
                stack_size += 1
        return min(len(nums),stack_size) 
        
```

C++思路相同，就不写了

#### 有序数组中出现次数超过25%的元素

==**（二分法）**==

根据题目要求，满足条件的整数 x 至少在数组 `arr` 中出现了 `span = arr.length / 4 + 1` 次，那么我们可以断定：数组 `arr `中的元素` arr[0]`, `arr[span]`, `arr[span * 2]`, ... 一定包含 `x`。

我们可以使用反证法证明上述的结论。假设` arr[0]`, `arr[span]`, `arr[span * 2]`, ... 均不为` x`，由于数组 `arr `已经有序，那么 x 只会连续地出现在 `arr[0]`, `arr[span]`, `arr[span * 2]`, ... 中某两个相邻元素的间隔中，因此其出现的次数最多为` span - 1` 次，这与它至少出现 `span` 次相矛盾。

既然`arr[0]`, `arr[span]`, `arr[span * 2]` ... 中肯定有x，设置` for i in range(0,n,span)`循环，这样的话`arr[i]`中必出x，我们在每个区间上进行查找，得到其在 `arr` 中出现的位置区间。如果该区间的长度至少为 `span`，那么我们就得到了答案。

> 反证：` arr[0]`, `arr[span]`, `arr[span * 2]`间隔为span +1，除去端点2个，即span - 1，由有序数组条件……

- `bisect.bisect_left` 是 Python 标准库 `bisect` 中的一个函数，用于在已排序的数组 `arr` 中找到 `arr[i]` 第一次出现的位置。例如，如果数组是 `[1, 2, 2, 3]`，`arr[i]` 为 2，那么 `bisect_left` 会返回 1。
- `bisect.bisect_right` 同样是 `bisect` 库中的函数，用于在已排序的数组 `arr` 中找到 `arr[i]` 最后一次出现的位置的下一个位置。例如，如果数组是 `[1, 2, 2, 3]`，`arr[i]` 为 2，那么 `bisect_right` 会返回 3。

``` python
# 双指针遍历法
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        slow , cnt = 0, 1
        n = len(arr)
        for fast in range(1,n):
            if arr[fast] == arr[slow] :
                cnt += 1
                slow += 1
                if cnt * 4 > n:
                    return arr[fast]
            else :
                cnt , slow = 1,fast
        if cnt * 4 > n:
            return arr[slow]
        
# 二分法
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        span = len(arr) // 4 + 1

        for i in range(0,len(arr),span):
            iter_left = bisect.bisect_left(arr,arr[i])
            iter_right = bisect.bisect_right(arr,arr[i])
            if iter_right - iter_left >= span :
                return arr[i]
        return -1

```

``` C++
```





#### 最小绝对差

* **海象运算符**

海象运算符的基本语法是 `变量名 := 表达式`，它会计算表达式的值，并将该值赋给变量名，同时整个表达式返回这个值。

在这个例子中，由于海象运算符，`cur=b-a`，且生命周期在整个`for`中

* **`pairwise()`**

`pairwise` 是 Python 标准库 `itertools` 模块中的一个函数，它用于从一个可迭代对象中生成相邻元素对。

> 下面是对`pairwise()`的示例：

``` python
from itertools import pairwise

numbers = [1, 2, 3, 4, 5]
输出：(1, 2)	(2, 3)	(3, 4)	(4, 5)	
for pair in pairs:
    print(pair) 

输出：
1 2
2 3
3 4
4 5	
for a,b in  pairwise(numbers):
    print(a,b)
```



* **题解**

``` python
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        m , ans = inf , []
        for a,b in pairwise(arr):
            if (cur := b - a ) < m:
                m , ans = cur , [[a,b]]
            elif ( b - a ) == m:
                ans.append([a,b])
        return ans

```



* **`emplace_back`：**效果同`push_back`
* **`initializer_list`：**用于表示整数类型的初始化列表。

``` C++
class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        sort(arr.begin(),arr.end());
        int n = arr.size();
        int best = INT_MAX;
        vector<vector<int>> ans;
        for(int i = 0;i < n- 1; ++ i)
        {
            if(int delta = arr[i+1] - arr[i];delta < best)
            {
                best = delta;
                ans = {{arr[i],arr[i+1]}};
            }
            else if( delta == best)
            {
                ans.emplace_back(initializer_list<int>{arr[i],arr[i+1]});
            }
        }
        return ans;
    }
};
```



#### 合并两个有序数组

为什么倒着用双指针？

> nums1后n个空间是空的，倒着可以避免覆盖

``` python
//双指针倒序法
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 ,p2 ,p = m-1, n-1 ,m+n-1
        # while：保证p2有元素就一直执行循环
        while p2 >= 0:
            # 若nums1[p1] < nums2[p2]，最终会使p1<0，之后一直执行else内容
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p -= 1
                p1 -= 1
            else :
                nums1[p] = nums2[p2]
                p -= 1
                p2 -= 1
            
```

C++思路不变



#### 两个数组的交集

``` python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = set(nums1)
        res = []
        for x in nums2:
            if x in st:
                st.remove(x)
                res.append(x)
        return res
```

``` C++
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;
        set<int> st(nums1.begin(),nums1.end());
        for(auto &x : nums2)
        {
            auto it = st.find(x);
            if (it != st.end())//找到了
            {
                st.erase(x);
                res.push_back(x);
            }
        }
        return res;
    }
};
```

