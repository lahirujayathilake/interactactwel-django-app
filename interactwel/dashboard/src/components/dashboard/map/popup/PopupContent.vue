<template>
    <div>
        <strong>Name: </strong>{{ data.name }}<br>
        <strong>Data Availability: </strong> {{ data.data_Range}}<br>
        <strong>Observation Type: </strong>{{ data.obs_type}}<br>
        <strong>Num. of Precipitation Obs.: </strong>{{ data.num_Pobs}}<br>
        <strong>Num. of Temperature Obs.: </strong>{{ data.num_Tobs}}

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
