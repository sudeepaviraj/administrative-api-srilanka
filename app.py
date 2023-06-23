from flask import Flask,jsonify
import json
from flask import request
from Database import SelectQuery

app = Flask(__name__)

@app.route("/")
def Home():
    return '''
    <h1 id="sri-lanka-administrative-data-api">Sri Lanka Administrative Data API</h1>
<p>👋 Welcome to the Sri Lanka Administrative Data API repository! This API provides access to provinces, districts, and division data in Sri Lanka.</p>
<h2 id="installation">Installation</h2>
<ol>
<li>Clone the repository:</li>
</ol>
<pre><code class="lang-bash">git <span class="hljs-keyword">clone</span> <span class="hljs-title">https</span>://github.com/sudeepaviraj/administrative-api-srilanka.git
</code></pre>
<ol>
<li>Navigate to the project directory:</li>
</ol>
<pre><code class="lang-bash"><span class="hljs-built_in">cd</span> administrative-api-srilanka
</code></pre>
<ol>
<li>Install the required dependencies:</li>
</ol>
<pre><code class="lang-bash">pip <span class="hljs-keyword">install</span> -r requirements.txt
</code></pre>
<h2 id="config">Config</h2>
<p>You Need to configure this application before use</p>
<ol>
<li>Create a database named <code>srilankav2</code> in your sql server </li>
</ol>
<ol>
<li>Import <code>srilanka.sql</code> to your own sql server</li>
</ol>
<ol>
<li>Create a <code>.env</code> file and add database connection values </li>
</ol>
<pre><code><span class="hljs-attr">DATABASE_HOST</span>=<span class="hljs-string">"YOUR DATABASE HOST"</span>
<span class="hljs-attr">DATABASE_PORT</span>=<span class="hljs-string">"YOUR DATABASE PORT"</span>
<span class="hljs-attr">DATABASE_USER</span>=<span class="hljs-string">"YOUR DATABASE USER"</span>
<span class="hljs-attr">DATABASE_PASSWORD</span>=<span class="hljs-string">"YOUR DATABASE PASSWORD"</span>
<span class="hljs-attr">DATABASE_NAME</span>=<span class="hljs-string">"srilankav2"</span>
</code></pre><h2 id="usage">Usage</h2>
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
<li><strong>Get all divisions in a district</strong>: <code>/getdivisons?district={district_id}</code></li>
<li><p><strong>Get all villages in a division</strong>: <code>/villages?division={division_id}</code></p>
</li>
<li><p>Make HTTP GET requests to the desired endpoints using tools like <code>curl</code> or <code>Postman</code> to retrieve the administrative data.</p>
</li>
</ol>
<p>Example request using <code>curl</code>:</p>
<pre><code class="lang-bash">curl <span class="hljs-string">http:</span><span class="hljs-comment">//localhost:5000/provinces</span>
</code></pre>
<p>Example response:</p>
<pre><code class="lang-json">[   
  [
    <span class="hljs-number">63</span>,
    <span class="hljs-string">"Western"</span>,
    <span class="hljs-string">"බස්නාහිර"</span>,
    <span class="hljs-string">"மேற்கு"</span>
  ],
  [
    <span class="hljs-number">64</span>,
    <span class="hljs-string">"Central"</span>,
    <span class="hljs-string">"මධ්‍යම"</span>,
    <span class="hljs-string">"மத்திய"</span>
  ]
]
</code></pre>
<h2 id="response-structure">Response Structure</h2>
<p><code>provinces,districts and divisions</code></p>
<pre><code class="lang-json"> [
   <span class="hljs-string">"PROVINCE_ID"</span>,
   <span class="hljs-string">"NAME_EN"</span>,
   <span class="hljs-string">"NAME_SI"</span>,
   <span class="hljs-string">"NAME_TA"</span>
 ]
</code></pre>
<pre><code class="lang-villages```">```json
 [
   [
    <span class="hljs-string">"LIFE_CODE"</span>,
    <span class="hljs-string">"GN_CODE"</span>,
    <span class="hljs-string">"MPA_CODE"</span>,
    <span class="hljs-string">"NAME_EN"</span>,
    <span class="hljs-string">"NAME_SI"</span>,
    <span class="hljs-string">"NAME_TA"</span>
  ]
 ]
</code></pre>
<h2 id="demo-api-endpoint">Demo API Endpoint</h2>
<pre><code class="lang-http://db.famed.cloud/```">
<span class="hljs-comment">## *Special Note*</span>

**You can <span class="hljs-built_in">run</span> sql queries form your own <span class="hljs-built_in">application</span> directly. To do <span class="hljs-keyword">that</span> please use database <span class="hljs-built_in">file</span> ```srilanka.sql``` <span class="hljs-keyword">to</span> your own mysql server**

<span class="hljs-comment">## Contributing</span>

We welcome contributions <span class="hljs-keyword">to</span> improve this project! If you'd like <span class="hljs-keyword">to</span> contribute, please follow these steps:

<span class="hljs-number">1.</span> Fork <span class="hljs-keyword">the</span> repository.

<span class="hljs-number">2.</span> Create a new branch <span class="hljs-keyword">for</span> your feature:

```bash
git checkout -b feature/your-feature-<span class="hljs-built_in">name</span>
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
    provinces = SelectQuery("SELECT id,name_en,name_si,name_ta FROM provinces")
    print(json.dumps({"provinces":provinces}))
    return json.dumps(provinces)

@app.route("/districts",methods=["GET"])
def DistrictsList():
    districts= SelectQuery("SELECT id,name_en,name_si,name_ta FROM districts")
    return json.dumps(districts)

@app.route("/getdistricts",methods=["GET"])
def DistrictsListSELECT():
    id = request.args.get("province")
    if id is None:
        return "Please Add Province Id",422
    else:
        districts = SelectQuery(f"SELECT id,name_en,name_si,name_ta FROM districts WHERE province_id = {id}")
        print(districts)
        return districts

@app.route("/divisions",methods=["GET"])
def DivisionsList():
    divisions= SelectQuery("SELECT id,name_en,name_si,name_ta FROM divisions")
    return json.dumps(divisions)

@app.route("/getdivisions",methods=["GET"])
def DivisionsListSELECT():
    id = request.args.get("district")
    if id is None:
        return "Please Add District Id", 422
    else:
        divisions = SelectQuery(f"SELECT id,name_en,name_si,name_ta FROM divisions WHERE district_id = {id}")
        return json.dumps(divisions)

@app.route("/villages",methods=["GET"])
def VillagesListSELECT():
    id = request.args.get("division")
    if id is None:
        return "Please Add Division Id", 422
    else:
        divisions = SelectQuery(f"SELECT life_code, gn_code, mpa_code, name_en, name_si,name_ta FROM villages WHERE division_id = {id}")
        return json.dumps(divisions)




if __name__ == "__main__":
    app.run(debug=True)