<template>
    <nav class="navbar is-dark">
        <div class="navbar-brand">
            <router-link to="/" class="navbar-item">
                <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false">
                <span aria-hidden="false"></span>
                <span aria-hidden="false"></span>
                <span aria-hidden="false"></span>
                </a>
                
                
            </router-link>
        </div>

        <div class="navbar-menu">
            <div class="navbar-end">
                <div class="navbar-item">
                    <div class="buttons">
                        <router-link to="/sign-up" class="button is-success"><strong>Sign Up</strong></router-link>
                        <router-link to="/log-in" class="button is-light">Log in</router-link>
                    </div>
                </div>
            </div>   
        </div>
    </nav>

         
</template>

<script>
    export default {
        name: 'Navbar'
    }
</script>