<template>
    <div>
        <h1>Recommendation System</h1>
        <br>
        <div id="base">
        <div class="sub-head">
            <h3>Select any three movies and rate them accordingly</h3>
        </div>
            <ul id="sglist">
                <li class="movies" v-for="(suggestion,idx) in suggestions" :key="idx" 
                    v-on:mouseover="fadeIn(idx)" v-on:mouseleave="fadeOut(idx)">
                        <div>{{ suggestion.title}}</div> 
                        <div>{{ suggestion.year}}</div>
                    <div id="rate" v-if="suggestion.active || suggestion.rating">
                        <p class="rate-head">Rate this Movie</p>
                        <div id="rating">
                            <StarRating :star-size="30" :increment="0.5" :show-rating="false" @rating-selected="setRating"></StarRating>
                            <p class="rate-text" v-if="suggestion.rating"> You have selected {{ suggestion.rating }} stars</p>
                            <p class="rate-text" v-else> No rating selected</p>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
         <div class="modalone" role="dialog" v-if="len > 3">
            <div class="modal-dialog modal-dialog-centered" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title"></h5>
                    </div>
                    <div class="modal-body">
                        Thank you for telling us what you like
                        Click on Next to see our Recommendations
                        </div>
                    <div class="modal-footer">
                        <router-link to="/recommendations">
                        <button type="button" class="btn btn-secondary" @click = "submit">Next</button>
                        </router-link>
                    </div>
                </div>
            </div>
        </div>
        <router-view></router-view>
    </div>
</template>

<script>
import axios from 'axios';
import StarRating from 'vue-star-rating';

export default {
    name: "Home",
    components: {
        StarRating,
    },
    data() {
        return {
            suggestions: '',
            userInput:[],
            len: 0,
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
        },
    methods: {
        fadeIn(index){
            this.$set(this.suggestions[index],'active',true)
        },
        fadeOut(index){
            this.$set(this.suggestions[index],'active',false)
        },
        setRating(rating) {
            for (var i=0;i<24;i+=1){
                if (this.suggestions[i].active == true){
                    this.$set(this.suggestions[i],'rating',rating);
                    this.userInput.push(
                    {"title":this.suggestions[i].title,
                    "rating": rating
                    });
                    this.len +=1;
                }
            }
        },
        submit() {
            const path = "http://127.0.0.1:5000/send";
            axios.post(path,this.userInput)
            .then(()=>{
            })
            .catch((err)=>{
                console.log(err);
            });
        }


    }
    
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

#rate {
    background:rgba(0,0,0,0.75);
    width:100%;
    height:100%;
    top: 0;
    /* right: 0; */
    position: absolute;
    /* bottom: 0; */
    left: 0;
    z-index:2;
    padding: 10px;
}
.rate-head {
    top: 5;
    color: white;
}
.sub-head {
    text-align:left;
    margin-left: 6rem;
    display: flex;
    justify-content: space-between;
    max-width: 84%;
}

#rating {
    bottom: 0;
}

.rate-text {
    margin-top:10px;
    font-weight:bold;
    color:white;
}

.modalone {
    display: block;
    background: rgba(0,0,0,0.5);
    position: fixed;
    top: 0;
    left: 0;
    z-index: 1050;
    width: 100%;
    height: 100%;
    overflow: hidden;
    outline: 0;
}
router-link {

}
</style>