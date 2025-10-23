import React from "react";
import "./Resultado.css";
import Header from "../Header";
import imagemGrafico from "../../images/analytics.jpg"

const Resultado = () => {
  return (
    <div className="Resultado">
      <Header />
      <div className="detalhes">
        <h2>Descubra os detalhes do seu perfil</h2>
        <div className="dadosUser">
          <div className="usuario">
            <p>Nome: Macedão</p>
            <p>Data de Nascimento: 02/06/1980</p>
            <p>Talentos: Programar as coisas</p>
          </div>
          <div className="graphic">
            <img src={imagemGrafico}></img>
          </div>
        </div>
        <div class="table-container">
          <table class="disc-table">
            <thead>
              <tr>
                <th>D</th>
                <th>I</th>
                <th>S</th>
                <th>C</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>5,00</td>
                <td>30,83</td>
                <td>-4,67</td>
                <td>-5,45</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="text-container">
    <div class="paragraph">
      <div class="disc-label">D</div>
      <p>
       	Quis non sit dui duis class rutrum convallis augue urna ultrices, aenean cubilia quam nam auctor netus tempor metus luctus, dolor sit tristique donec id dui proin leo quisque. vivamus enim mattis aliquet libero eros massa in cubilia maecenas venenatis, ipsum tempus ultricies class praesent suscipit porttitor magna libero, quis erat accumsan in scelerisque tellus erat cras velit. class leo vestibulum aenean ipsum libero pretium, ultricies ac habitasse conubia maecenas 
      </p>
    </div>

    <div class="paragraph">
      <div class="disc-label">I</div>
      <p>
        	Quis non sit dui duis class rutrum convallis augue urna ultrices, aenean cubilia quam nam auctor netus tempor metus luctus, dolor sit tristique donec id dui proin leo quisque. vivamus enim mattis aliquet libero eros massa in cubilia maecenas venenatis, ipsum tempus ultricies class praesent suscipit porttitor magna libero, quis erat accumsan in scelerisque tellus erat cras velit. class leo vestibulum aenean ipsum libero pretium, ultricies ac habitasse conubia maecenas 
      </p>
    </div>

    <div class="paragraph">
      <div class="disc-label">S</div>
      <p>
       	Quis non sit dui duis class rutrum convallis augue urna ultrices, aenean cubilia quam nam auctor netus tempor metus luctus, dolor sit tristique donec id dui proin leo quisque. vivamus enim mattis aliquet libero eros massa in cubilia maecenas venenatis, ipsum tempus ultricies class praesent suscipit porttitor magna libero, quis erat accumsan in scelerisque tellus erat cras velit. class leo vestibulum aenean ipsum libero pretium, ultricies ac habitasse conubia maecenas 
      </p>
    </div>

    <div class="paragraph">
      <div class="disc-label">C</div>
      <p>
       	Quis non sit dui duis class rutrum convallis augue urna ultrices, aenean cubilia quam nam auctor netus tempor metus luctus, dolor sit tristique donec id dui proin leo quisque. vivamus enim mattis aliquet libero eros massa in cubilia maecenas venenatis, ipsum tempus ultricies class praesent suscipit porttitor magna libero, quis erat accumsan in scelerisque tellus erat cras velit. class leo vestibulum aenean ipsum libero pretium, ultricies ac habitasse conubia maecenas 
      </p>
    </div>
  </div>
      </div>
    </div>
  )
};

export default Resultado;
