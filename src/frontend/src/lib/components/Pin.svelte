<script>
    import { onMount } from 'svelte';

    let digits = new Array(6)

    onMount(()=> {
        document.getElementById("0")?.focus()
    })
    
    function nextDigit(id) {
        console.log(digits)
        document.getElementById(id + 1)?.focus()
    }
</script>
<div class="pin">
    <from class="pin-form">
        <input type="hidden">
        {#each digits as digit, i}
            <input class="form-control digit" type="number"
            id={i.toString()} min=0 max=9 
            on:input={() => {nextDigit(i)}} bind:value={digits[i]}>
        {/each}
    </from>

</div>

<style>
    .digit {
        max-width: 40px;
        -moz-appearance: textfield;
    }
    .pin-form {
        max-width: 320px;
        
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-around;
        margin: auto;
    }

</style>