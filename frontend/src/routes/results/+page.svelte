<script lang="ts">
  import { onMount } from 'svelte';

  let results: Record<string, number> = {};

  onMount(async () => {
    await fetchResults();
  });

  async function fetchResults() {
    const res = await fetch('http://localhost:5000/results');
    results = await res.json();
  }

  async function clearData() {
    const res = await fetch('http://localhost:5000/clear', { method: 'POST' });
    if (res.ok) {
      await fetchResults();
    }
  }
</script>

<style>
  .bar {
    background-color: rgb(0, 158, 150);
    height: 30px;
    display: flex;
    align-items: center;
    color: white;
    border-radius: 1px;
    padding: 0 0px;
  }

  .clear-button {
    padding: 5px 5px;
    background-color: rgb(244, 160, 160);
    color: white;
    border: none;
    cursor: pointer;
    border-radius: 4px;
  }
  .grid {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 40vh;
    gap: 20px;
    border-radius: 4px;
  }

  .result-grid {
    display: flex;
    justify-content: left;
    flex-direction: row;
    gap: 10px;
    width: 100%;
    padding: 2px;
  }
  .letter {
    display: flex;
    justify-content: center;
    align-items: center;
  }

</style>

<div class='grid'>
  <ul>
    {#each ['A', 'B', 'C', 'D'] as option}
      <div class='result-grid'>
        <div class='letter'>{option}</div>
        {#if results[option]}
          <div class="bar" style="width: {results[option] * 20}px;"> {results[option]}</div>
        {:else}
          <div class="bar" style="width: 0px;">0</div>
        {/if}
      </div>
    {/each}
  </ul>

  <button class='clear-button' on:click={clearData}>Nové hlasování</button>
</div>
