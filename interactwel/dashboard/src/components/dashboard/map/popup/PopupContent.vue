<template>
    <div>
        This is the  {{ data.name }}
    </div>
</template>

<script>
    export default {
        name: "PopupContent",
        props: {
            data: {
                name: String
            }
        }
    };
</script>
