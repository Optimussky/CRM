<template>
    <nav class="navbar is-dark">
        <div class="navbar-brand">
            <router-link to="/" class="navbar-item">
                <strong> CRM</strong>
                <!-- <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false">
                <span aria-hidden="false"></span>
                <span aria-hidden="false"></span>
                <span aria-hidden="false"></span>
                </a> -->
                
                
            </router-link>
        </div>

        <div class="navbar-menu">
            <div class="navbar-end">                
                <router-link to="/dashboard" class="navbar-item">Dashboard</router-link>
                <router-link to="/dashboard/leads" class="navbar-item">Leads</router-link>
                <div class="navbar-item">
                    <template v-if="!$store.state.isAuthenticated">
                        <div class="buttons">
                            <router-link to="/sign-up" class="button is-success"><strong>Sign Up</strong></router-link>
                            <router-link to="/log-in" class="button is-light">Log in</router-link>
                        </div>
                    </template>
                    
                    <template v-else>
                        
                        <router-link to="/dashboard/my-account" class="button is-info">My Account</router-link>
                    </template>

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