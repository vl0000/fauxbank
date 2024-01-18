<script>
    import { goto } from "$app/navigation";
    import { onMount } from 'svelte';

    // check for a valid session
    onMount(() => {
        goto('/account')
    })
</script>