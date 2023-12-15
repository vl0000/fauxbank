<script>
    // should load this data from the server
    const symbol = "R$"

    const data = {
        balance: 1500.00
    }
</script>
<div class="accountbalance">
    <span>Balance</span>
    <div id="balance">
        {symbol} {data.balance}
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