<script>
    import AccountBalance from "$lib/components/AccountBalance.svelte";
    import AccountInfo from "$lib/components/AccountInfo.svelte";
    import TransactionList from "$lib/components/TransactionList.svelte";

</script>

<div class="row" id="top">
    <AccountInfo />
</div>
<div class="row" id="balance">
    <AccountBalance />    
</div>
<div class="row" id="latest-transactions">
    <TransactionList title={"Latest transactions"} />
</div>
<style>
    #top {
        height: 8vh;
    }
    #balance {
        height: 16vh;
        align-content: space-around;
    }
    #latest-transactions {
        height: 60vh;
    }
</style>