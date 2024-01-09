<script>
    import AccountBalance from "$lib/components/AccountBalance.svelte";
    import Card from "$lib/components/Card.svelte";
    import DashButtons from "$lib/components/DashButtons.svelte";
    import TransactionList from "$lib/components/TransactionList.svelte";

</script>


<AccountBalance />
<Card />
<DashButtons />
<TransactionList title="Latest Transaction"/>

<style>
    .blue {
        background-color: aqua;
    }
</style>