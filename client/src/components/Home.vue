<template>
    <div>
        <h1>Recommendation System</h1>
        <br>
            <ul id="sglist">
                <li class="movies" v-for="suggestion in suggestions" :key="suggestion.title">
                    
                    <div>{{ suggestion.title}}</div> 
                    <div>{{ suggestion.year}}</div>
                </li>
            </ul>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: "Home",
    data() {
        return {
            suggestions: '',
        }
    },
    created: function() {
            const path = "http://127.0.0.1:5000/";
            axios.get(path)
                .then((res)=>{
                    this.suggestions = res.data;
                })
                .catch((err)=>{
                    console.log(err);
                });
        }
    
}

</script>

<style>
#sglist {
    list-style: none;
    display: flex;
    flex-wrap: wrap;
    max-width: 100%; 
    justify-content:center;
    margin: auto;
    padding:0;
}

.movies {
    width: 200px;
    height: 250px;
    padding: 20px;
    border: solid 1px;
    margin: 1rem 1rem;
}
</style>