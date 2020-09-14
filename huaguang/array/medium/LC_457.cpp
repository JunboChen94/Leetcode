//457. Circular Array Loop
//
//You are given a circular array nums of positive and negative integers.If a number k at an index is positive, then move forward k steps.Conversely, 
//if it's negative (-k), move backward k steps. Since the array is circular, you may assume that the last element's next element is the first element, 
//and the first element's previous element is the last element.
//
//Determine if there is a loop(or a cycle) in nums.A cycle must startand end at the same indexand the cycle's length > 1. Furthermore, movements in a 
//cycle must all follow a single direction. In other words, a cycle must not consist of both forward and backward movements.
//
//
//
//Example 1:
//Input: [2, -1, 1, 2, 2]
//Output : true
//Explanation : There is a cycle, from index 0 -> 2 -> 3 -> 0. The cycle's length is 3.
//
//Example 2 :
//Input : [-1, 2]
//Output : false
//Explanation : The movement from index 1 -> 1 -> 1 ... is not a cycle, because the cycle's length is 1. By definition the cycle's length must be greater than 1.
//
//Example 3 :
//Input : [-2, 1, -1, -2, -2]
//Output : false
//Explanation : The movement from index 1 -> 2 -> 1 -> ... is not a cycle, because movement from index 1 -> 2 is a forward movement, but movement from index 2 -> 1 
//is a backward movement.All movements in a cycle must follow a single direction.


#include<iostream>
#include<vector>

using namespace std;
class Solution {
public:
	bool circularArrayLoop(vector<int>& nums) {
		vector<int> check;
		for (int i = 0; i < nums.size(); i++) {
			if (has_circle(i, nums, check)) return true;
		}
		return false;
	}
};

int get_nexe_element(int idx, vector<int>& nums) {
	if (idx + nums[idx] > (nums.size() - 1)) return (idx + nums[idx] - nums.size());
	else if (idx + nums[idx] < 0) return(idx + nums[idx] + nums.size());
	else return (idx + nums[idx]);
}

bool has_circle(int idx, vector<int>& nums, vector<int> check) {
	int new_idx;
	new_idx = get_nexe_element(idx, nums);
	if (nums[idx] == nums[new_idx] || (nums[idx] * nums[new_idx] < 0)) return false;
	else {
		for (int j = 0; j < check.size(); j++) {
			if (new_idx == check[j]) return true;
		}
		check.push_back(new_idx);
	}
	return has_circle(new_idx, nums, check);
}


int main() {
	vector<int> test = { 2,-1,1,2,2 };
	Solution so;

	bool result;
	result = so.circularArrayLoop(test);

	cout << "The result is : " << result;
}


///////Better Solution

//思路
//对每个元素查找是否有环，终止条件如下：
//
//1.如果下一个元素是本身，则不可能有环；
//2.如果下一个元素在本次查找中出现过，则有环；
//3.如果下一个元素的正负号相反，则不可能有环。
//
//实现
//关键点
//1.下一个元素下标计算；
//2.终止条件的判断顺序；
//3.不需要重复判定查找过的元素。



//class Solution {
//public:
//	bool circularArrayLoop(vector<int>& nums) {
//		// 记录哪些元素被查找过，已查找过的不再查找
//		vector<int> visited(nums.size(), 0);
//		for (int i = 0; i < nums.size(); i++) {
//			if (visited[i]) continue;
//			vector<int> vs(nums.size(), 0);
//			// 对每个元素判断是否有环
//			if (has_circular(nums, vs, i)) {
//				return true;
//			}
//			else {
//				// 将本次查找过的元素加入无需找找的列表
//				for (int i = 0; i < nums.size(); i++)
//					if (vs[i]) visited[i] = vs[i];
//			}
//		}
//		return false;
//	}
//	// 取下一个元素的下标
//	int get_index(vector<int>& nums, int i) {
//		int res = i + nums[i];
//		while (res < 0) res += nums.size();
//		return res % nums.size();
//	}
//
//	bool has_circular(vector<int>& nums, vector<int>& visited, int i) {
//		int next = get_index(nums, i);
//		// 先判定下一个元素是否是自己
//		if (next == i) {
//			visited[i] = true;
//			return false;
//		}
//		// 下一个元素出现在当次遍历，则成功找到环
//		if (visited[next]) return true;
//		// 符号相反不可能有环
//		if (nums[next] > 0 != nums[i] > 0) return false;
//		visited[next] = true;
//		// 继续查找
//		return has_circular(nums, visited, next);
//	}
//};