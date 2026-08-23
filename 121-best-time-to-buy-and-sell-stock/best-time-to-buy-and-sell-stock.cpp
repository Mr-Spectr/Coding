#include <vector>
#include <algorithm>

class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        if (prices.empty()) {
            return 0; 
        }

        int minPrice = prices[0];
        int maxProfit = 0;       
        for (size_t i = 1; i < prices.size(); ++i) {
            int currentProfit = prices[i] - minPrice;
            maxProfit = std::max(maxProfit, currentProfit);
            minPrice = std::min(minPrice, prices[i]);
        }

        return maxProfit; 
    }
};
