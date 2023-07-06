<script>
    import { onMount } from 'svelte';
    
    let results = {};
  
    onMount(async () => {
      const res = await fetch('http://localhost:5000/results');
      results = await res.json();
    });
  </script>
  
<h1>Vote results</h1>
<ul>
{#each Object.entries(results) as [option, count] (option)}
    <li>{option}: {count}</li>
{/each}
</ul>
