<template>
    <div>
        <h1>Here are the movies which you would like</h1>
        <div id="base">
            <ul id="sglist">
                <li class="movies" v-for="(recommendation,idx) in recommendations" :key="idx">
                        <div>{{ recommendation.title}}</div> 
                        <div>{{ recommendation.year}}</div>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: "Recommendation",
    data() {
        return {
            recommendations:'',
        }
    },
    created: function() {
        const path = "http://127.0.0.1:5000/response";
        axios.get(path)
            .then((res)=>{
                this.recommendations = res.data;
            })
            .catch((err)=>{
                console.log(err);
            });
    },
}
</script>

<style>
#base {
    max-width: 100%;
    margin: auto;
}
#sglist {
    list-style: none;
    display: flex;
    flex-wrap: wrap;
    padding:0;
    justify-content:center; 
}

.movies {
    width: 200px;
    height: 250px;
    padding: 20px;
    border: solid 1px;
    margin: 1rem 1rem;
    position:relative;
}


</style>