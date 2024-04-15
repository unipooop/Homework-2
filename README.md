# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution:
The rationale behind subtracting a minimum liquidity upon initial liquidity minting in the mint function of the UniswapV2Pair contract is to ensure that the liquidity provider (LP) is adding a sufficient amount of liquidity to the pool. This helps prevent cases where LPs might add negligible amounts of liquidity that could potentially disrupt the efficient functioning of the automated market maker (AMM) mechanism.

By imposing a minimum liquidity requirement, Uniswap ensures that LPs are incentivized to contribute meaningful liquidity that enhances the depth and stability of the liquidity pool. This helps maintain optimal trading conditions for users and ensures that trades can be executed with minimal slippage.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution：
The intention behind using a specific formula for obtaining liquidity when depositing tokens (not for the first time) in the minting function of the UniswapV2Pair contract is to maintain a proportional relationship between the liquidity in the pool and the quantity of tokens deposited. By employing this formula, Uniswap ensures that each token deposit is adjusted according to market demand and supply, thereby ensuring the efficiency and stability of the liquidity pool. This design allows for obtaining corresponding liquidity regardless of the quantity of tokens deposited, without compromising market liquidity.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution
One occurs before the victim transaction, while the other follows it, creating a ‘sandwich’ of transactions with the victim in the middle which gives the attack its name.First, the attacker identifies a potential victim transaction. This will typically be one with high slippage tolerance, which offers better profit potential. The fees included in the transaction can also increase its susceptibility to sandwich attacks.Once found, the attacker moves to send a buy transaction for the same asset pair which will fill before the user’s transaction. This is done by setting a higher fee rate to move the tokens to the DEX, and is known as ‘frontrunning’.This attacker transaction shifts the liquidity pool composition, resulting in the available exchange rates for subsequent transactions being different to that which was originally shown to other users whose transactions have not yet executed.

Once the victim swap completes at the unfavorable exchange rate, the attacker follows up with a sell transaction for the asset pair which locks in their profit. This second transaction ‘backruns’ the victim, completing the sandwich.

