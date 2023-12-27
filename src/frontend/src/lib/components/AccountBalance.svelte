<script>
    // should load this data from the server
    import { account } from "../../stores";

    const symbol = "R$"

</script>
<div class="accountbalance">
    <span>Balance</span>
    <div id="balance">
        {symbol} {$account.balance}
    </div>
</div>
<style>
    .accountbalance {
        font-size: 24px;
        line-height: 100%;
        
        text-align: start;
    }

    #balance {
        font-size: 32px
    }
</style>