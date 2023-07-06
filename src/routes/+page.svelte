<script>
    let selection = "";
    
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
  

<div>
  {#each options as option (option)}
    <label>
      <input type="radio" bind:group={selection} value={option}>
      {option}
    </label>
  {/each}
</div>

<button on:click={vote}>Vote</button> 

