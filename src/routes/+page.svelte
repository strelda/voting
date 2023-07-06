<script lang='ts'>
    let selection = "";
    function selectOption(option: string): void {
    selection = option;
  }

    function vote() {
      fetch('http://localhost:5000/vote', {
        method: 'POST',
        body: JSON.stringify({ option: selection }),
        headers: { 'Content-Type': 'application/json' },
      })
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => console.log(data))
      .catch(error => {
        console.log('There was a problem with the fetch operation: ', error.message);
      });
    }
  
    const options = ['A', 'B', 'C', 'D'];
</script>

<div class='grid'>
  <div class="button-grid">
    {#each options as option (option)}
      <button on:click={() => selectOption(option)} class:selected={selection === option}>{option}</button>
    {/each}
  </div>

  <button class="vote-button" on:click={vote}>Vote</button>
</div>

<style>
  .grid {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    gap: 10px;
  }

  .button-grid {
    display: flex;
    justify-content: center;
    flex-direction: column;
    gap: 10px;
    width: 90%;
  }

  .button-grid button {
    flex: 1;
    padding: 30px;
    background-color: rgb(41, 71, 71);
    color: white;
    border: none;
    text-align: center;
    cursor: pointer;
    border-radius: 20px;
  }

  .button-grid button.selected {
    background-color: rgb(0, 158, 150);
  }

  .vote-button {
    padding: 10px 20px;
    background-color: rgb(35, 146, 70);
    color: white;
    border: none;
    cursor: pointer;
    border-radius: 20px;
  }
</style>
