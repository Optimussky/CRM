<template>
    <nav class="navbar is-dark">
        <div class="navbar-brand">
            <router-link to="/" class="navbar-item">
                <strong> CRM</strong>

                
                
            </router-link>
        </div>

        <div class="navbar-menu">
            <div class="navbar-end">  
                
                <template v-if="$store.state.isAuthenticated">
                    <router-link to="/dashboard" class="navbar-item">Dashboard</router-link>
                    <router-link to="/dashboard/leads" class="navbar-item">Leads</router-link>
                    <router-link to="/dashboard/my-account" class="button is-info">My Account</router-link>
                </template>
                    
                <!--<router-link to="/dashboard" class="navbar-item" v-if="$store.state.isAuthenticated">Dashboard</router-link>
                <router-link to="/dashboard/leads" class="navbar-item" v-if="$store.state.isAuthenticated">Leads</router-link>-->
                
                <div class="navbar-item">
                    <template v-if="!$store.state.isAuthenticated">
                        <div class="buttons">
                            <router-link to="/sign-up" class="button is-success"><strong>Sign Up</strong></router-link>
                            <router-link to="/log-in" class="button is-light">Log in</router-link>
                        </div>
                    </template>
                    
                    <!--<template v-else>
                        
                        <router-link to="/dashboard/my-account" class="button is-info">My Account</router-link>
                    </template>
                    -->

                    

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