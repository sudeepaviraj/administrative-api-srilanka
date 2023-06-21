from flask import Flask,jsonify
import json
from flask import request
from Database import SelectQuery

app = Flask(__name__)

@app.route("/")
def Home():
    return '''<h1 id="sri-lanka-administrative-data-api">Sri Lanka Administrative Data API</h1>
<p>👋 Welcome to the Sri Lanka Administrative Data API repository! This API provides access to provinces, districts, and division data in Sri Lanka.</p>
<h2 id="installation">Installation</h2>
<ol>
<li>Clone the repository:</li>
</ol>
<pre><code class="lang-bash">git <span class="hljs-keyword">clone</span> <span class="hljs-title">https</span>://github.com/sudeepaviraj/gn-extract.git
</code></pre>
<ol>
<li>Navigate to the project directory:</li>
</ol>
<pre><code class="lang-bash"><span class="hljs-built_in">cd</span> gn-extract
</code></pre>
<ol>
<li>Install the required dependencies:</li>
</ol>
<pre><code class="lang-bash">pip <span class="hljs-keyword">install</span> -r requirements.txt
</code></pre>
<h2 id="usage">Usage</h2>
<ol>
<li>Run the application:</li>
</ol>
<pre><code class="lang-bash"><span class="hljs-keyword">python</span> app.<span class="hljs-keyword">py</span>
</code></pre>
<ol>
<li><p>Once the application is running, you can access the API endpoints:</p>
</li>
<li><p><strong>Get all provinces</strong>: <code>/provinces</code></p>
</li>
<li><strong>Get all districts</strong>: <code>/districts</code></li>
<li><strong>Get all divisions</strong>: <code>/divisions</code></li>
<li><strong>Get all districts in a province</strong>: <code>/getdistricts?province={province_id}</code></li>
<li><p><strong>Get all divisions in a district</strong>: <code>/getdivisons?district={district_id}</code></p>
</li>
<li><p>Make HTTP GET requests to the desired endpoints using tools like <code>curl</code> or <code>Postman</code> to retrieve the administrative data.</p>
</li>
</ol>
<p>Example request using <code>curl</code>:</p>
<pre><code class="lang-bash">curl <span class="hljs-string">http:</span><span class="hljs-comment">//localhost:5000/provinces</span>
</code></pre>
<p>Example response:</p>
<pre><code class="lang-json">[
    {
        <span class="hljs-attr">"id"</span>: <span class="hljs-number">1</span>,
        <span class="hljs-attr">"name"</span>: <span class="hljs-string">"Western"</span>
    },
    {
        <span class="hljs-attr">"id"</span>: <span class="hljs-number">2</span>,
        <span class="hljs-attr">"name"</span>: <span class="hljs-string">"Central"</span>
    },
    ...
]
</code></pre>
<h2 id="demo-api">Demo API</h2>
<p>You can access the demo of this project from</p>
<pre><code><span class="hljs-symbol">http:</span><span class="hljs-comment">//db.famed.cloud/</span>
</code></pre><h2 id="contributing">Contributing</h2>
<p>We welcome contributions to improve this project! If you&#39;d like to contribute, please follow these steps:</p>
<ol>
<li><p>Fork the repository.</p>
</li>
<li><p>Create a new branch for your feature:</p>
</li>
</ol>
<pre><code class="lang-bash">git checkout -b <span class="hljs-built_in">feature</span>/your-<span class="hljs-built_in">feature</span>-name
</code></pre>
<ol>
<li>Make your changes and commit them:</li>
</ol>
<pre><code class="lang-bash"><span class="hljs-attribute">git</span> commit -m <span class="hljs-string">"Add your commit message"</span>
</code></pre>
<ol>
<li>Push your changes to your forked repository:</li>
</ol>
<pre><code class="lang-bash">git <span class="hljs-built_in">push</span> <span class="hljs-built_in">origin</span> <span class="hljs-built_in">feature</span>/your-<span class="hljs-built_in">feature</span>-name
</code></pre>
<ol>
<li>Open a pull request, and we&#39;ll review your changes.</li>
</ol>
<h2 id="license">License</h2>
<p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>
'''

@app.route("/provinces",methods=["GET"])
def ProvincesList():
    provinces = SelectQuery("SELECT * FROM provinces")
    print(json.dumps({"provinces":provinces}))
    return json.dumps(provinces)

@app.route("/districts",methods=["GET"])
def DistrictsList():
    districts= SelectQuery("SELECT id,name FROM districts")
    return json.dumps(districts)

@app.route("/getdistricts",methods=["GET"])
def DistrictsListSELECT():
    id = request.args.get("province")
    if id is None:
        return "Please Add Province Id",422
    else:
        districts = SelectQuery(f"SELECT id,name FROM districts WHERE province_id = {id}")
        print(districts)
        return districts

@app.route("/divisions",methods=["GET"])
def DivisionsList():
    divisions= SelectQuery("SELECT id,name FROM divisions")
    return json.dumps(divisions)

@app.route("/getdivisions",methods=["GET"])
def DivisionsListSELECT():
    id = request.args.get("district")
    if id is None:
        return "Please Add District Id", 422
    else:
        divisions = SelectQuery(f"SELECT id,name FROM divisions WHERE district_id = {id}")
        return json.dumps(divisions)


if __name__ == "__main__":
    app.run(debug=True)