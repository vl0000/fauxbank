<script>
    // should load this data from the server
    import { account } from "../../stores";

    const symbol = "R$"

</script>
<div class="accountbalance">

    <span>Balance</span>
    <span id="ammout">{symbol} {$account.balance}</span>
</div>
<style>
    .accountbalance {
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;

        grid-area: balance;
        font-size: 24px;
        line-height: 100%;
        text-align: start;
        
        background-color: black;
        color: white;
        margin: 0px 6px 0px 6px;
        padding: 0px 20px 5px 20px;
        border-radius: 10px;

        font-size: 20px;
    }

    #ammout {
        font-size: 40px;
        margin-top: 8px;
    }
</style>