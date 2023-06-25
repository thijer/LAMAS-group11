<template>
  <v-container class="">
    <v-responsive class="align-center text-center">
      <!-- <v-img height="300" src="@/assets/logo.svg" /> -->

      <div class="text-body-2 font-weight-light mt-5 mb-n0">Lamas Group 11</div>

      <h1 class="text-h2 font-weight-bold">Epistemic Reasoning in Computer Networks</h1>
      <!-- <h1 class="text-h3 font-weight-bold"></h1> -->

      <div class="py-5" />


      <v-row>
        <v-col>
          <v-card @click="scrollToElement('Introduction')" color="primary">
            <v-card-title>
              Introduction
            </v-card-title>
          </v-card>
        </v-col>
        <v-col>
          <v-card @click="scrollToElement('Formalism')" color="primary">
            <v-card-title>
              Formalism
            </v-card-title>
          </v-card>
        </v-col>
        <v-col>
          <v-card @click="scrollToElement('Simulation')" color="primary">
            <v-card-title>
              Simulation
            </v-card-title>
          </v-card>
        </v-col>
        <v-col>
          <v-card @click="scrollToElement('Discussion')" color="primary">
            <v-card-title>
              Discussion
            </v-card-title>
          </v-card>
        </v-col>
        
      </v-row>

      <v-row class="d-flex align-center justify-center pa-5 text-justify" id="intro">
        <v-col cols="auto">
          <v-sheet>
            <h1 class="text-h4 font-weight-bold" id="Introduction">Introduction</h1>
            <p>Modern computer networks, consist of multiple dispersed systems that communicate and collaborate. 
                Often these networks will have to maintain a consensus
                with regard to the information on the network. Each node in the network has
                its knowledge and beliefs about the state of the network, the transactions, or
                events that occur, and the behaviour of other nodes. Epistemic logic can help
                capture and reason about this distributed knowledge and belief structure.
            </p>
            <p>
              Epistemic logic is a branch of logic that deals with knowledge and belief.
              It provides a formal framework for reasoning about what agents in a system
              know or believe, and how their knowledge and beliefs evolve. In the context
              of decentralized computer networks, epistemic logic can be used to model and
              reason about the knowledge and beliefs of the nodes in the network.
            </p>
            <p>
              There are many ways in which epistemic logic can be applied to modern de-
              centralized computer systems: knowledge representation, fault tolerance, con-
              sensus protocols, and reasoning regarding security and privacy.
            </p>
            <p>
              This paper focuses on how decentralized systems can use epistemic logic to
              model knowledge on the systems. This can be achieved by nodes reasoning
              about the knowledge and beliefs of nodes in the presence of faulty nodes. Nodes
              can use epistemic logic to reason about the reliability of information on a system
              and the knowledge of other nodes on the systems.
            </p>
            <p>
              In this project, we aim to evaluate the propagation of knowledge through
              a distributed system, where nodes (or processors) are sparsely connected to
              each other. For instance, new knowledge obtained by node A which can be a
              sensor reading needs to be transferred throughout the network so all the nodes
              know about it, which can be done with a cascade of private announcements.
              Additionally, knowledge can also be updated so facts that were valid at t are
              not valid at <span class="font-italic">t + 1</span>.
            </p>
          </v-sheet>
        </v-col>
      </v-row>

      <v-row class="d-flex align-center justify-center pa-5  text-justify">
        <v-col cols="auto">
          <v-sheet>
            <h1 class="text-h4 font-weight-bold" id="Formalism">Formalism</h1>
            
          </v-sheet>
        </v-col>
      </v-row>

      <v-row class="d-flex align-center justify-center pa-5  text-justify">
        <v-col cols="auto">
          <v-sheet>
            <h1 class="text-h4 font-weight-bold" id="Simulation">Simulation</h1>
          </v-sheet>
        </v-col>
      </v-row>


      <v-row class="d-flex align-center justify-center pa-5  text-justify" id="Discussion">
        <v-col cols="auto">
          <v-sheet>
            <h1 class="text-h4 font-weight-bold" ref="discussion">Discussion</h1>

          </v-sheet>
        </v-col>
      </v-row>
    </v-responsive>
  </v-container>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  //


  function scrollToElement(el) {
      const element = document.getElementById(el)
      element.scrollIntoView({ behavior: "smooth" })
  }
</script>
