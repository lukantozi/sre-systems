#include <stdio.h>

int maxProfit(int* prices, int pricesSize) {
    int profit = 0;
    int buy_ind = 0;
    int sell_ind = 1;
    while (sell_ind < pricesSize) {
        if (prices[sell_ind] > prices[buy_ind]) {
            if (profit < prices[sell_ind] - prices[buy_ind]) {
                profit = prices[sell_ind] - prices[buy_ind];
            }
            sell_ind++;
        } else {
            buy_ind = sell_ind;
            sell_ind++;
        }
    }
    return profit;
}

int main(void) {
    int prices[11] = {1,2,4,2,5,7,2,4,9,0,9};
    int prof = maxProfit(prices, 11);
    //int prices[5] = {7,6,4,3,1};
    //int prof = maxProfit(prices, 5);
    //int prices[6] = {7,1,5,3,6,4};
    //int prof = maxProfit(prices, 6);
    printf("Profit is: %d\n", prof);
}
