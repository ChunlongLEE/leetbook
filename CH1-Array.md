

## 数组

### 数组的基本算法设计

#### **1.移除元素**

* **双指针/快慢指针**

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

* **元素移动法**

用k来记录值为`val`的个数，k为0则无事发生，k不为0的话，`nums[i]`往前的`k`个位置就是它的目的地

``` python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                k += 1
            else :
                nums[i - k] = nums[i]
        return len(nums) - k
```

``` C++
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0;
        for(int i = 0;i < nums.size() ; ++i)
        {
            if (nums[i] == val)
            {
                k++;
            }
            else
            {
                nums[i - k] = nums[i];
            }
        }
        return nums.size() - k;
    }
};
```

* **双指针交换法**

  在遍历过程中，对于每个元素`nums[i]`检查它是否等于目标值`val`

  * 如果 `nums[i]` 不等于 `val`，说明这个元素需要保留。此时将指针 `j` 向后移动一位，因为 `j` 指针要指向新的非目标值元素应该存放的位置，即下一个`!=val`的值放的位置
  * 接着检查 `j` 是否不等于 `i`。如果 `j` 不等于 `i`，说明有等于`val`的值，也即当前不等于 `val` 的元素不在它应该在的位置（即 `j` 所指向的位置），需要进行交换操作，将 `nums[i]` 和 `nums[j]` 的值进行交换，从而把不等于 `val` 的元素移到数组的前面。

  把整个数组分成三个区间：

  * 保留区：`[0 , j] `； 故长度为`j + 1`
  * 删除区：之后的区间

``` python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = -1
        for i in range(len(nums)):
            if nums[i] != val:
                j += 1
                if j != i : 
                    nums[i] , nums[j] = nums[j] , nums[i]
        return j + 1
```



``` C++
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int j = -1;
        for(int i = 0 ; i < nums.size();++i)
        {
            if(nums[i] != val)
            {
                j ++;
                if (j != i)
                {
                    swap(nums[i],nums[j]);
                }
            }
        }
        return j + 1;
    }
};
```



#### 2.移动零

* **整体建表(双指针)**

把0看成上一题的`val`，删除所有0，再在表末添加0即可

``` python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        while slow < len(nums):
            nums[slow] = 0
            slow += 1
```

``` C++
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i = 0,j = 0;
        for(;j < nums.size();++j)
        {
            if(nums[j] != 0)
            {
                nums[i++] = nums[j];
            }
        }
        for(;i < nums.size();++i)
        {
            nums[i] = 0;
        }
        
    }
};
```



* **元素移动法(k)**

同上题，将0看成`val`，先将所有0删除再移动数组，最后在数组末补充0

此方法中，k记录的是0的个数，故最后添0时，从`len(nums)-k`开始赋值

``` python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                k += 1
            else :
                nums[i - k] = nums[i]
        # 将数组末尾的 k 个位置置为 0
        for j in range(len(nums) - k, len(nums)):
            nums[j] = 0
```

````C++
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int k = 0;
        for(int i = 0 ; i < nums.size() ;++i)
        {
            if(nums[i] != 0)
            {
                nums[i - k] = nums[i];
            }
            else
            {
                k ++;
            }
        }
        for (int j = nums.size() - k ; j < nums.size(); ++j)
        {
            nums[j] = 0;
        }
    }
};
````



* **区间划分法(双指针交换)**

``` python
# 区间划分法--双指针交换法
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        # 一旦fast扫描到0，fast和slow便有了差距；并且slow的指向一定是下一个非0元素应该在的位置
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow],nums[fast] = nums[fast],nums[slow]
                slow += 1
                
```

``` C++
// 区间划分法--双指针交换法
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
```

* **入栈法(法二移动元素法的另一种写法)**

``` python
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

* **整体建表法---快慢指针**

``` python
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        slow = 0 
        for fast in range(len(nums)):
            if nums[fast] == 0:
                continue
            else:
                if fast + 1 < len(nums)  and nums[fast] == nums[fast + 1]:
                    nums[fast] *= 2
                    nums[fast + 1] = 0
                nums[slow] = nums[fast]
            slow += 1
        for i in range(slow , len(nums)):
            nums[i] = 0
        return nums
```

``` C++
class Solution {
public:
    vector<int> applyOperations(vector<int>& nums) {
        int n = nums.size();
        int slow = 0;
        for (int fast = 0 ; fast < n ; ++fast)
        {
            if (nums[fast] == 0)
            { continue ;}
            else 
            {
                if ( fast + 1 < n && nums[fast] == nums[fast + 1])
                {
                nums[fast] *= 2;
				nums[fast + 1] = 0;   
                }
            //只要没有0，fast和slow不会拉开差距，便一直是原地赋值；
            //且假如有若干个0使slow和fast有差距，此时slow一定指向0，此时便用fast的值完成覆盖
            nums[slow ++] = nums[fast];
            }
        }
        for (int i = slow ;i < n ; ++i)
        {
            nums[i] = 0;
        }
        return nums;
    }
};
```



* **元素移动法**

``` python
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        k = 0
        for fast in range(len(nums)):
            if nums[fast] == 0:
                k += 1
            else:
                if fast + 1 < len(nums) and nums[fast] == nums[fast + 1]:
                    nums[fast] *= 2
                    nums[fast + 1] = 0
                nums[fast - k] = nums[fast]
            
        for i in range(len(nums) - k , len(nums)):
            nums[i] = 0
        return nums 
```



``` C++
class Solution {
public:
    vector<int> applyOperations(vector<int>& nums) {
        int n = nums.size();
        int slow = 0;
        int k = 0;
        for (int fast = 0 ; fast < n ; ++ fast)
        {
            if (nums[fast] == 0)
            {
                k++;
                continue ;
            }
            else //nums[fast]!=0的情况：
            {
                //顺手的事
                if (fast + 1 < n && nums[fast] == nums[fast + 1])
                {
                    nums[fast] *= 2;
                    nums[fast + 1] = 0;
                }
                nums[fast - k] = nums[fast];//最好放在else内，因为逻辑为：nums[fast]!=0时，就要执行该语句
            }  
        }
        for (int i = n - k ; i < n ;++i)
        {
            nums[i] = 0;
        }
        return nums;
    }
    
};
```



* **区间划分法--双指针交换**

``` python
# 区间划分法--双指针交换
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        j = 0
        for i in range(len(nums)):
            if i+1 < len(nums) and nums[i] == nums[i+1]  :
                nums[i] *= 2
                nums[i+1] = 0
            # 并非else，因为同时要判断这个if
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

#### 4.颜色分类

* **区间划分法(双指针交换)**
  * `nums[j]`为下一个0应存放的位置，`j`指针左边都应为0
  * `nums[k]`为下一个2应存放的位置，`k`指针右边都应为2
  * 中间的位置为1

``` python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i , j , k = 0 , -1 , len(nums)
        while i < k:
            if nums[i] == 0:
                j += 1
                if i != j:
                    nums[i] , nums[j] = nums[j] , nums[i]
                i += 1
            elif nums[i] == 2:
                k -= 1
                if i != k :
                    nums[i] , nums[k] = nums[k] , nums[i]
            else : 
                i += 1
```



``` C++
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int j = -1, i = 0 , k = nums.size();
        while  (i < k)
        {
     		//扫描到0和2都要将其交换到自己应在的区间范围，对于1，不需要管它，处理好0和2的位置，1的位置也便是正确的
            if (nums[i] == 0 )
            {
                j++;
                if(i != j)
                {
                    swap(nums[i] , nums[j]);
                }
                i++;
            }
            else if (nums[i] == 2)
            {
                k--;
                if(i != k)
                {
                    swap(nums[i],nums[k]);
                }
            }
            else // 扫描到1
            {
                i++;
            }
        } 

    }
};
```

* **排序计数法**

hash表的思想，设置`vector<int> hash`，记录`nums`中0，1，2的数量；再输出即可

``` python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hash = [0] * 3
        for num in nums:
            hash[num] += 1
        k = 0
        for i in range(3):
            for j in range(hash[i]):
                nums[k] = i
                k += 1
        
```



``` C++
class Solution {
public:
    void sortColors(vector<int>& nums) {
        vector<int> hash(3,0);
        for(int i = 0 ; i < nums.size(); ++i)
        {
            hash[nums[i]]++;
        }
        int k = 0;
        for(int i = 0 ; i < 3 ; ++i)
        {
            for(int j = 0; j < hash[i] ; ++j)
            {
                nums[k++] = i; 
            }
        }
    }
};
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
            # 有序数组删除重复项，这意味着每个数字只保留一次，nums[fast]与nums[fast-1]一定不能相同
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
class Solution {
public:
    int findSpecialInteger(vector<int>& arr) {
        int  cnt = 1 , n = arr.size();
        int cur = arr[0];
        //提问：当写成cnt = 0 以及for(int i = 0;……)时，可不用再for循环结束后判断cnt*4的值，为何？
        for( int i = 1 ; i < arr.size(); ++i)
        {
            if(arr[i] == cur)
            {
                cnt += 1;
                if(cnt * 4 > n)
                {
                    return arr[i];
                }
            }
            else
            {
                cnt = 1;
                cur = arr[i];
            }
        }//for
        if (cnt * 4 > n)
        {
            return cur;
        }//if
        
        return -1;
};
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
            # 当nums1走到头或者nums1的值 < nums2的值时，执行else语句
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p -= 1
                p1 -= 1
            # 当nums1走到头时，便开始一直执行else
            else :
                nums1[p] = nums2[p2]
                p -= 1
                p2 -= 1
            
```

C++思路不变



``` C++
//C++双指针正向暴力法
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> ans(m + n);
        int i = 0 , j = 0 , p = 0;
        while (i < m && j < n)
        {
            if (nums1[i] < nums2[j])
            {
                ans[p++] = nums1[i++];
            }
            else
            {
                ans[p++] = nums2[j++];
            }
        }
        while(i < m)
        {
            ans[p] = nums1[i];
        }
        while(j < n)
        {
            ans[p] = nums2[j];
        }
        return ans;
    }
};
```



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

#### 有序数组的平方(双指针一次遍历)

使用初始化列表的话，这个题没什么难度了，且消耗比较大

``` python
# 最简单方法：
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [num ** 2 for num in nums]
        ans.sort()
        return ans
```

``` C++
//最简单方法：
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> ans;
        for(auto &num : nums)
        {
            ans.push_back(num * num) ;
        }
        sort(ans.begin(),ans.end());
        return ans;
    }
};
```

==双指针==

已知序列是升序的，正着遍历，不会知道负数平方和正数平方的大小；在不使用内置函数的情况下

设置首尾指针，平方大的放在新数列的尾部

``` python
# 双指针
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        i , j , p = 0 , n - 1 , n - 1
        while i <= j:
            if nums[i]**2  < nums[j] ** 2:
                ans[p] = nums[j] ** 2
                j -= 1
            else :
                ans[p] = nums[i] ** 2
                i += 1
            p -= 1
        return ans 
  
```

C++思路相同，略

#### 重新排列数组

``` python
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums[::2] , nums[1::2] = nums[:n] , nums[n:]
        return nums
```



``` c++
class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> ans(2*n);
        for (int i = 0 , j  = n , p = 0 ; i < n || j < 2 * n ; )
        {
            ans[p++] = nums[i++];
            ans[p++] = nums[j++];
        }
        return ans;
    }
};
```

#### 三个有序数组的交集

``` 
```

#### 丑数Ⅱ

**python建堆**

* **`heapq`模块**：提供`heappop()`和`heappush()`
  * `heappop()`：从堆中弹出并返回最小的元素，同时保持堆的性质。这里的堆是基于列表实现的，所以它可以操作列表类型的数据，但它并非列表的内置方法。
  * `heappush(heap,nxt)`：将元素 `nxt` 插入到已有的堆 `heap` 中，并且维持堆的性质不变。这里的堆是基于列表实现的，而堆的性质通常指的是小顶堆，也就是堆中每个节点的值都小于或等于其子节点的值。

``` python
# python建堆

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 丑数：1，2……
        # n = 1，不需建堆，n = 2只需建一次堆，……
        seen = {1}
        factor = [2,3,5]
        heap = [1]
        for i in range(n  - 1):
            cur = heapq.heappop(heap)
            for fac in factor:
                if (nxt := fac * cur) not in seen :
                    seen.add(nxt)
                    heapq.heappush(heap , nxt)
        return heapq.heappop(heap)

```

**C++建堆(优先队列)**

`unordered_set`：无序

`priority_queue` 是一个优先队列容器适配器，它可以实现堆的功能。`priority_queue` 的基本语法如下：

```C++
std::priority_queue<Type, Container, Compare> pq;
```

- `Type`：表示优先队列中元素的类型，例如该题中的 `long`。
- `Container`：表示优先队列底层使用的容器，通常使用 `vector` 或 `deque`，默认是 `vector`。
- `Compare`：表示元素的比较方式，默认是 `less<Type>`，即大顶堆；如果要创建小顶堆，需要使用 `greater<Type>`。

``` C++
class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> factors = { 2,3,5};
        priority_queue<long,vector<long>,greater<long>> heap;
        unordered_set<long>seen ;
        seen.insert(1L);
        heap.push(1L);
        int ugly = 0;
        for (int i = 0 ; i < n ;++i)
        {
            long cur = heap.top();
            heap.pop();
            ugly = (int)cur;
            for (int &fac :factors)
            {
                long next = fac * cur ;
                if (!seen.count(next))
                {
                    seen.insert(next);
                    heap.push(next);
                }
            }
        }
        return ugly;
        //
    }
};
```

**动态规划**

```` python
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        p2 = p3 = p5 = 1
        # 因为dp[0]不放元素，从dp[1]开始，n个数就需要n+1个空间
        for i in range(2,n + 1):# 【2，n+1)一共n个数
            num2 , num3 , num5 = dp[p2] * 2,dp[p3] * 3,dp[p5] * 5 
            dp[i]  = min(num2,num3,num5)
            if dp[i] == num2:
                p2 += 1
            # num2,num3,num5有相等的情况下，相等的指针都要++；所以不能用if---elif
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
        return dp[n]
````

C++动态规划思路同，略

####  查找和最小的 k 对数字

规定` (i,j−1)` 出堆时，将 `(i,j) `入堆；而 `(i−1,j)` 出堆时只计入答案，其它什么也不做。

换句话说，在` (i,j) `出堆时，只需将` (i,j+1)` 入堆，无需将 `(i+1,j) `入堆。

但若按照该规则，初始仅把 (0,0) 入堆的话，只会得到 (0,1),(0,2),⋯ 这些下标对。

> 这就是下面代码第一个if语句的原因

所以初始不仅要把 (0,0) 入堆，(1,0),(2,0),⋯ 这些都要入堆。

代码实现时，为了方便比较大小，实际入堆的是三元组 `(a[i]+b[j],i,j)`。

``` python
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        heap = [(nums1[0] + nums2[0] , 0 , 0)]
        while len(ans) < k:
            _, i , j = heappop(heap)
            ans.append([nums1[i],nums2[j]])
            # 
            if j == 0 and i + 1 < len(nums1):
                heappush(heap , (nums1[i + 1] + nums2[j] , i + 1 ,j))
            if j + 1 < len(nums2):
                heappush(heap , (nums1[i] + nums2[j + 1] , i , j + 1))
        return ans 
```



#### 加一

* python的简易做法

``` python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_num = "".join(str(_) for _ in digits)
        int_num = int(str_num) + 1
        return [int(i) for i in str(int_num)]
```

* 算法思想

  当我们对数组 digits 加一时，我们只需要关注 digits 的末尾出现了多少个 9 即可。我们可以考虑如下的三种情况：

  * 如果 digits 的末尾没有 9，例如 [1,2,3]，那么我们直接将末尾的数加一，得到 [1,2,4] 并返回；
  * 如果 digits 的末尾有若干个 9，例如 [1,2,3,9,9]，那么我们只需要找出从末尾开始的第一个不为 9 的元素，即 3，将该元素加一，得到 [1,2,4,9,9]。随后将末尾的 9 全部置零，得到 [1,2,4,0,0] 并返回。
  * 如果 digits 的所有元素都是 9，例如 [9,9,9,9,9]，那么答案为 [1,0,0,0,0,0]。我们只需要构造一个长度比 digits 多 1 的新数组，将首元素置为 1，其余元素置为 0 即可。

``` C++
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
        for(int i = n - 1 ; i >= 0 ;--i)
        {
            if(digits[i] != 9)
            {
                digits[i]++;
                for(int j = i + 1 ; j < n  ; ++ j)
                {
                    digits[j]  = 0;
                }
            return digits;
            }   
        }
        vector<int> ans(n + 1);
        ans[0] = 1;
        return ans;
    }
};
```

