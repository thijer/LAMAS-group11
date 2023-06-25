<template>
  <v-container class="">
    <v-responsive class="align-center text-center">
      <!-- <v-img height="300" src="@/assets/logo.svg" /> -->

      <div class="text-body-2 font-weight-light mt-5 mb-n0">Lamas Group 11</div>

      <h1 class="text-h2 font-weight-bold">Epistemic Reasoning in Computer Networks</h1>
      <a href="https://github.com/thijer/LAMAS-group11" target="_blank">https://github.com/thijer/LAMAS-group11</a>
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
          <v-card @click="scrollToElement('example')" color="primary">
            <v-card-title>
              Example
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
        <v-col>
          <v-card @click="scrollToElement('References')" color="primary">
            <v-card-title>
              References
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
              There are many ways in which epistemic logic can be applied to modern decentralized
              computer systems: knowledge representation, fault tolerance, consensus
              protocols, and reasoning regarding security and privacy.
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
            <h1 class="text-h5 font-weight-bold">Research</h1>
            <p>
              Our research question is:
            </p>
            <p class="font-italic text-center">Can the knowledge propagated using private announcements in a decentralized
              system be accurately modelled using Kripke models?</p>
            <p>The model would need to accurately model the various worlds created by
              the network structure and the traffic routing. The various nodes in the network
              would be the agents in our model, the routing of traffic would govern their
              knowledge and belief about the state of the network. We have included private announcements
              for node communication and created both a simple model
              with reliable agents and one that models a network that contains an amount of
              unreliable agents</p>
          </v-sheet>
        </v-col>
      </v-row>

      <v-row class="d-flex align-center justify-center pa-5  text-justify">
        <v-col cols="auto">
          <v-sheet>
            <h1 class="text-h4 font-weight-bold" id="Formalism">Formalism</h1>
            <h1 class="text-h5 font-weight-bold">Dynamic Epistemic Logic</h1>
            <p>Dynamic Epistemic Logic (DEL) is an extension of traditional epistemic logic,
              extending static states of knowledge and belief, incorporating dynamic operators
              that represent actions and informational updates. Allowing us to reason about
              the effects of actions on knowledge and belief, as well as the informational
              consequences of communication between agents.</p>
            <p>
              In DEL, agents are characterized by their knowledge and beliefs. For example,
              the operator <em>K</em><sub>a</sub>Φ represents “Agent a knows that Φ,” indicating that agent
              a is certain about the truth of φ. Similarly, the operator B<sub>a</sub>φ represents “Agent
              a believes that φ” indicating that agent a considers φ to be true, but may not
              be certain.
            </p>
            <p>
              DEL introduces additional operators to represent actions and informational
              updates. The action operators describe the effects of actions on agents’ knowledge
              and beliefs. For instance, the operator [α]φ represents the result of performing
              an action α, which leads to the formula φ being true in the resulting
              state. Actions here are not restricted to physical actions, we can also allow for
              epistemical actions.
            </p>
            <h1 class="text-h5 font-weight-bold">Network models</h1>
            <p>A network model is a graph where the vertices indicate agents and the edges
              indicate communication channels between agents. Each agent has a knowledge
              base KB being a set of propositional atoms. The union of all knowledge bases
              constitutes the system knowledge K.</p>
            <p>From each network model, a Kripke model can be derived, which is done
              as follows: a × 2<sup>n</sup> worlds are created, where n is the number of atoms in the
              system knowledge K and a the number of agents. Each agent therefore has a
              copy of all possible atom valuation combinations, which can be thought of as
              the agent’s perspective P of the knowledge in the system. A visualization of a
              Kripke model with no knowledge about p can be found in figure 2.</p>
            <p>A relation between world <em>w</em><sub>0</sub> and <em>w</em><sub>1</sub> for agent a is made if:</p>
            <br>
            <p class="text-p2 text-center"><span
                class="math display">(¬(¬<em>π</em><sub><em>p</em></sub>(<em>w</em><sub>1</sub>)∧<em>w</em><sub>0</sub>∈<em>P</em><sub><em>a</em></sub>∧<em>w</em><sub>1</sub>∈<em>P</em><sub><em>a</em></sub>)
                for all
                <em>p</em>∈<em>K</em><em>B</em><sub><em>a</em></sub>) ∧ <em>w</em><sub>1</sub> ∈ <em>P</em><sub><em>a</em></sub></span>
            </p>
            <br>
            <p>
              where <em>π</em><sub><em>p</em></sub>(<em>w</em><sub>1</sub>) is the valuation of <em>p</em> in world
              <em>w</em><sub>1</sub>, <em>P</em><sub><em>a</em></sub> the set of worlds belonging
              to agent a’s perspective, and <em>K</em><em>B</em><sub><em>a</em></sub> the knowledge base of a.
            </p>
            <p>This can be translated roughly to that there will be no relation from a world
              <em>w</em><sub>0</sub> in the agent’s perspective to a world <em>w</em><sub>1</sub> in the agent’s
              perspective where p
              doesn’t hold if p is in the agents’ knowledge base, or if the relation points to a
              world <em>w</em><sub>1</sub> not in the agent’s perspective
            </p>

            <h1 class="text-h5 font-weight-bold">Private announcements</h1>
            <p>Dynamic Epistemic Logic includes announcements in which information is communicated
              to agents. A common form of these announcements are public announcements
              the announcement operator [!φ]Φ represents an announcement of
              φ to all agents, resulting in the formula Φ becoming true in the updated state.
              For distributed computer networks, public announcements do not accurately
              represent how information is propagated through these systems. Typical information
              may be relayed across individual agents, and errors or broken links may
              lead to individual agents missing information.</p>
            <p>For our purposes, we will consider private announcements as a modification
              of public announcements, where only a subset of agents (or in a Kripke model,
              relations) are involved. A public announcement restricts the set of states to
              the states where the announcement holds. A private announcement restricts
              the relations of the agents involved to the states in the union of the involved
              agent’s perspectives where the announcement holds, and removes the others.
              The relations of uninvolved agents or relations coming from worlds outside the
              involved agent’s perspectives are untouched.</p>

            <p>For a private announcement involving n agents:</p>
            <p class="text-center"><span
                class="math inline"><em>P</em> = <em>P</em><sub>0</sub> ∪ ... ∪ <em>P</em><sub><em>n</em></sub></span>&emsp; Set
              of worlds included in the announcement.</p>
            <p class="text-center"><span class="math inline"><em>R</em> = {<em>R</em><sub>0</sub>, ...<em>R</em><sub><em>n</em></sub>}</span>
            &emsp; Set of all involved agent's relations.</p>


            <p>
              Private announcements will be implemented as an extension to the MLsolver
              implementation, so we can use it in combinations with the operators already
              defined.
            </p>
          </v-sheet>
        </v-col>
      </v-row>

      <v-row class="d-flex align-center justify-center pa-5  text-justify">
        <v-col cols="auto">
          <v-sheet>
            <h1 class="text-h4 font-weight-bold" id="example">Example Case</h1>
            <v-row class="d-flex align-center justify-center pa-5  text-justify">
              <v-col cols="auto">
                <v-card class="text-center" width="350">
                  <v-img class="text-center mx-auto" src="@/assets/s0_nw_model.png" :width="300"></v-img>
                  <v-card-title class="text-h6">
                    Figure 1
                    <br>
                    <!-- <span class="text-caption">caption</span> -->
                  </v-card-title>
                </v-card>
              </v-col>
            </v-row>
            <p>As an example to demonstrate private announcements, we consider a case where
              a person wants to buy something from Amazon. In this scenario, there are three
              parties: The Person, Amazon, and the Bank. Due to security and privacy reasons,
              the online transaction procedure is designed such that Amazon cannot
              access private banking information of the Person, and the bank cannot know
              the details and subject of the transaction between the Person and Amazon.
              This leads to the case where transaction progress is modelled with Private announcements.</p>
            <p>The associated network model of this example can be found in figure 1, where
              the edges indicate which agent can communicate with which agent. In this state,
              the payment has not yet been made. The corresponding Kripke model can be
              found in figure 2.</p>
            <v-row class="d-flex align-center justify-center pa-5  text-justify">
              <v-col cols="auto">
                <v-card class="text-center" width="auto">
                  <v-row>
                    <v-col>
                      <v-img class="text-center mx-auto" src="@/assets/s0_km_me.png" :width="figWidth"></v-img>
                    </v-col>
                    <v-col>
                      <v-img class="text-center mx-auto" src="@/assets/s0_km_amazon.png" :width="figWidth"></v-img>
                    </v-col>
                    <v-col>
                      <v-img class="text-center mx-auto" src="@/assets/s0_km_bank.png" :width="figWidth"></v-img>
                    </v-col>
                  </v-row> 
                  <v-card-title class="text-h6">
                    Figure 2
                    <br>
                    <!-- <span class="text-caption">caption</span> -->
                  </v-card-title>
                </v-card>
              </v-col>
              <v-col cols="auto">
                <v-card class="text-center" width="auto">
                  <v-row>
                    <v-col>
                      <v-img class="text-center mx-auto" src="@/assets/s1_km_me.png" :width="figWidth"></v-img>
                    </v-col>
                    <v-col>
                      <v-img class="text-center mx-auto" src="@/assets/s1_km_amazon.png" :width="figWidth"></v-img>
                    </v-col>
                    <v-col>
                      <v-img class="text-center mx-auto" src="@/assets/s1_km_bank.png" :width="figWidth"></v-img>
                    </v-col>
                  </v-row> 
                  <v-card-title class="text-h6">
                    Figure 3
                    <br>
                    <!-- <span class="text-caption">caption</span> -->
                  </v-card-title>
                </v-card>
              </v-col>
              <v-col cols="auto">
                <v-card class="text-center" width="auto">
                  <v-row>
                    <v-col>
                      <v-img class="text-center mx-auto" src="@/assets/s2_km_me.png" :width="figWidth"></v-img>
                    </v-col>
                    <v-col>
                      <v-img class="text-center mx-auto" src="@/assets/s2_km_amazon.png" :width="figWidth"></v-img>
                    </v-col>
                    <v-col>
                      <v-img class="text-center mx-auto" src="@/assets/s2_km_bank.png" :width="figWidth"></v-img>
                    </v-col>
                  </v-row> 
                  <v-card-title class="text-h6">
                    Figure 4
                    <br>
                    <!-- <span class="text-caption">caption</span> -->
                  </v-card-title>
                </v-card>
              </v-col>
              <v-col cols="auto">
                <v-card class="text-center" width="auto">
                  <v-row>
                    <v-col>
                      <v-img class="text-center mx-auto" src="@/assets/s3_km_me.png" :width="figWidth"></v-img>
                    </v-col>
                    <v-col>
                      <v-img class="text-center mx-auto" src="@/assets/s3_km_amazon.png" :width="figWidth"></v-img>
                    </v-col>
                    <v-col>
                      <v-img class="text-center mx-auto" src="@/assets/s3_km_bank.png" :width="figWidth"></v-img>
                    </v-col>
                  </v-row> 
                  <v-card-title class="text-h6">
                    Figure 5
                    <br>
                    <!-- <span class="text-caption">caption</span> -->
                  </v-card-title>
                </v-card>
              </v-col>
            </v-row>
              
            <p>
              The first private announcement happens between the Person and the Bank,
              when the Person confirms the payment to Amazon in the online transaction
              portal of the bank. As a result, both the Person and the Bank know that a
              payment has been made. This leads to the Kripke model in figure 3. Here we
              see that the ’knowledge’ (accessible worlds) for Amazon has not changed, but
              the Person and the Bank have their relations restricted to the worlds where p
              holds, with the exception of the relations coming from the worlds that constitute
              Amazon’s perspective or knowledge.
            </p>
            <p>
              The second private announcement happens between the Bank and Amazon,
              where the bank tells Amazon that the payment has been made. The Kripke
              model can be seen in figure 4. At this point, everyone knows that the payment
              has been made, but Amazon and the Person do not know of each other that they
              know (<span
                class="math inline"><em>M</em> ⊨ <em>E</em><em>p</em> ∧ ¬<em>K</em><sub><em>a</em></sub><em>K</em><sub><em>p</em></sub><em>p</em> ∧ ¬<em>K</em><sub><em>p</em></sub><em>K</em><sub><em>a</em></sub><em>p</em></span>).
              This means that p is not yet common
              knowledge. To remedy this, a final private announcement is made between
              Amazon and the Person, where Amazon tells the Person that the payment was
              successful. This is no new information for the Person, but the person is now
              aware that Amazon knows as well. This leads to the final Kripke model in figure
              5.
            </p>
          </v-sheet>
        </v-col>
      </v-row>

      <v-row class="d-flex align-center justify-center pa-5  text-justify">
        <v-col cols="auto">
          <v-sheet>
            <h1 class="text-h4 font-weight-bold" id="Simulation">Simulation</h1>
            <p>
              We aim to implement as part of our website a small simulation of a network
              evolving and the knowledge of the nodes, as well as the Kripke model representing
              this simulated network.
            </p>
            <p>The basis for the simulation is a so-called network model, which describes a
              set of agents, a knowledge base of propositional atoms for each agent, and a set
              of connections indicating which agent can communicate with each other. Such
              a network model can then be converted to a Kripke model, where the states are
              now defined by a combination of every propositional atom and their valuation.</p>
            <p>The way the model will evolve will cover the information propagating through
              the network, changes to the network including new nodes being added, nodes
              removed and temporary breaks in connections resulting in routing changes.</p>
          </v-sheet>
        </v-col>
      </v-row>


      <v-row class="d-flex align-center justify-center pa-5  text-justify" id="Discussion">
        <v-col cols="auto">
          <v-sheet>
            <h1 class="text-h4 font-weight-bold">Discussion</h1>
            <p>This project set out to model the propagation of knowledge through distributed
              systems using private announcements in a Kripke model. To achieve this, we
              extended the already useful MLSolver software to handle the propagation of epistemic
              information through distributed systems. This extension works through
              the introduction of private announcements. With these privately announcements
              being an appropriate representation of communication within distributed
              systems.</p>
            <p>Private announcements lead to ever more complex models, as the number
              of worlds increases dramatically as private announcements occur. With larger
              models with more systems, for example modelling a large blockchain, representing such
              systems may become computationally more complex.</p>
            <p>There are many ways this work could be extended. For one, additional
              elements of Dynamic Epistemic Logic could be added, further extending the
              utility of MLSolver. If this tool were to become a more useful tool for modelling
              distributed systems, it would need to be extended to include different types
              of errors seen in such systems. In its current state the solution models errors
              brought about by failed connections by omitting the private announcements
              between designated nodes. It cannot, however, model other errors such as the
              altering of information of a node. Such errors may come about due to faults
              or malicious actions, but it is clear that for distributed systems, such as a
              blockchain, to be fault-tolerant such errors must be included in a model.</p>
          </v-sheet>
        </v-col>
      </v-row>

      <v-row class="d-flex align-center justify-center pa-5  text-left" id="References">
        <v-col cols="auto">
          <v-sheet>
            <h1 class="text-h4 font-weight-bold" ref="references">References</h1>
            <ol>
              <li>J.-J. Ch. Meyer and W. van der Hoek. <em>Epistemic Logic for AI and Computer Science.</em>
                Cambridge Tracts in Theoretical Computer Science. Cambridge University Press, 1995. doi:
                10.1017/CBO9780511569852.
              </li>
              <li>Erik Rohkohl. <em>Modal logic solver.</em> <a
                  href="https://github.com/erohkohl/mlsolver">https://github.com/erohkohl/mlsolver</a>. 2017.
              </li>
              <li>Naomi Schraer. <em>Customers charged multiple times after Deliveroo app crash - here's ...</em> Sept.
                2018. <a
                  href="https://www.moneysavingexpert.com/news/2018/09/deliveroo-crash-leaves-customers-charged-multiple-times/226">https://www.moneysavingexpert.com/news/2018/09/deliveroo-crash-leaves-customers-charged-multiple-times/226</a>
              </li>
            </ol>
          </v-sheet>
        </v-col>
      </v-row>
    </v-responsive>
  </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue'
//
const figWidth = 250


function scrollToElement(el) {
  const element = document.getElementById(el)
  element.scrollIntoView({ behavior: "smooth" })
}
</script>
