
    

  

<!DOCTYPE html>
<html>
  <head>
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="chrome=1">
    <script type="text/javascript">var NREUMQ=[];NREUMQ.push(["mark","firstbyte",new Date().getTime()]);</script>
        <title>nodes/sonar.py at fe7c9224fbeba1411e2cd5b5fb0a00aa3a19f1df from heuristicus/auv-localisation-ros - GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />

    
    

    <meta content="authenticity_token" name="csrf-param" />
<meta content="842a806765a8d12ece48e35c2b0340e1acc42c3e" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/22cf97fc2e3dbcb593dc6a0092f68812794c864b/stylesheets/bundle_github.css" media="screen" rel="stylesheet" type="text/css" />
    

    <script type="text/javascript">
      if (typeof console == "undefined" || typeof console.log == "undefined")
        console = { log: function() {} }
    </script>
    <script src="https://a248.e.akamai.net/assets.github.com/javascripts/jquery/jquery-1.6.1.min.js" type="text/javascript"></script>

    <script type="text/javascript" charset="utf-8">
      var GitHub = {
        assetHost: 'https://a248.e.akamai.net/assets.github.com'
      }
      var github_user = 'heuristicus'

      
    </script>
    <script src="https://a248.e.akamai.net/assets.github.com/c95ebfaaef8d0756f7ecff3aad37542991891eb6/javascripts/bundle_github.js" type="text/javascript"></script>


    
    <script type="text/javascript" charset="utf-8">
      if (GitHub.spy) {
        GitHub.spy({repo: "heuristicus/auv-localisation-ros"});
      }
    </script>

    
  <link rel='permalink' href='/heuristicus/auv-localisation-ros/blob/fe7c9224fbeba1411e2cd5b5fb0a00aa3a19f1df/nodes/sonar.py'>

  <link href="https://github.com/heuristicus/auv-localisation-ros/commits/fe7c9224fbeba1411e2cd5b5fb0a00aa3a19f1df.atom" rel="alternate" title="Recent Commits to auv-localisation-ros:fe7c9224fbeba1411e2cd5b5fb0a00aa3a19f1df" type="application/atom+xml" />

    <META NAME="ROBOTS" CONTENT="NOINDEX, FOLLOW">

    <meta name="description" content="auv-localisation-ros - ros code for experiments for auv-localisation project" />
    <script type="text/javascript">
      GitHub.nameWithOwner = GitHub.nameWithOwner || "heuristicus/auv-localisation-ros";
      GitHub.currentRef = '';
      GitHub.commitSHA = "fe7c9224fbeba1411e2cd5b5fb0a00aa3a19f1df";
      GitHub.currentPath = 'nodes/sonar.py';
      GitHub.masterBranch = "master";

      
    </script>
  

        <script type="text/javascript">
      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-3769691-2']);
      _gaq.push(['_setDomainName', 'none']);
      _gaq.push(['_trackPageview']);
      _gaq.push(['_trackPageLoadTime']);
      (function() {
        var ga = document.createElement('script');
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        ga.setAttribute('async', 'true');
        document.documentElement.firstChild.appendChild(ga);
      })();
    </script>

    
  </head>

  

  <body class="logged_in page-blob linux env-production">
    

    

    

    <div class="subnavd" id="main">
      <div id="header" class="true">
          <a class="logo boring" href="https://github.com/">
            
            <img alt="github" class="default" height="45" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov6.png" />
            <!--[if (gt IE 8)|!(IE)]><!-->
            <img alt="github" class="hover" height="45" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov6-hover.png" />
            <!--<![endif]-->
          </a>

        
          





  
    <div class="userbox">
      <div class="avatarname">
        <a href="https://github.com/heuristicus"><img src="https://secure.gravatar.com/avatar/986ae440573f3f1bc8e98fa45c48d211?s=140&d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png" alt="" width="20" height="20"  /></a>
        <a href="https://github.com/heuristicus" class="name">heuristicus</a>

        
        
      </div>
      <ul class="usernav">
        <li><a href="https://github.com/">Dashboard</a></li>
        <li>
          
          <a href="https://github.com/inbox">Inbox</a>
          <a href="https://github.com/inbox" class="unread_count ">0</a>
        </li>
        <li><a href="https://github.com/account">Account Settings</a></li>
        <li><a href="/logout">Log Out</a></li>
      </ul>
    </div><!-- /.userbox -->
  


        
        <div class="topsearch">
  
    <form action="/search" id="top_search_form" method="get">
      <a href="/search" class="advanced-search tooltipped downwards" title="Advanced Search">Advanced Search</a>
      <div class="search placeholder-field js-placeholder-field">
        <label class="placeholder" for="global-search-field">Search…</label>
        <input type="text" class="search my_repos_autocompleter" id="global-search-field" name="q" results="5" /> <input type="submit" value="Search" class="button" />
      </div>
      <input type="hidden" name="type" value="Everything" />
      <input type="hidden" name="repo" value="" />
      <input type="hidden" name="langOverride" value="" />
      <input type="hidden" name="start_value" value="1" />
    </form>
    <ul class="nav">
      <li><a href="/explore">Explore GitHub</a></li>
      <li><a href="https://gist.github.com">Gist</a></li>
      
      <li><a href="/blog">Blog</a></li>
      
      <li><a href="http://help.github.com">Help</a></li>
    </ul>
  
</div>

      </div>

      
      
        
    <div class="site">
      <div class="pagehead repohead vis-public    instapaper_ignore readability-menu">

      

      <div class="title-actions-bar">
        <h1>
          <a href="/heuristicus">heuristicus</a> / <strong><a href="/heuristicus/auv-localisation-ros">auv-localisation-ros</a></strong>
          
          
        </h1>

        
    <ul class="actions">
      

      
        <li class="for-owner" style="display:none"><a href="/heuristicus/auv-localisation-ros/admin" class="minibutton btn-admin "><span><span class="icon"></span>Admin</span></a></li>
        <li>
          <a href="/heuristicus/auv-localisation-ros/toggle_watch" class="minibutton btn-watch " id="watch_button" onclick="var f = document.createElement('form'); f.style.display = 'none'; this.parentNode.appendChild(f); f.method = 'POST'; f.action = this.href;var s = document.createElement('input'); s.setAttribute('type', 'hidden'); s.setAttribute('name', 'authenticity_token'); s.setAttribute('value', '842a806765a8d12ece48e35c2b0340e1acc42c3e'); f.appendChild(s);f.submit();return false;" style="display:none"><span><span class="icon"></span>Watch</span></a>
          <a href="/heuristicus/auv-localisation-ros/toggle_watch" class="minibutton btn-watch " id="unwatch_button" onclick="var f = document.createElement('form'); f.style.display = 'none'; this.parentNode.appendChild(f); f.method = 'POST'; f.action = this.href;var s = document.createElement('input'); s.setAttribute('type', 'hidden'); s.setAttribute('name', 'authenticity_token'); s.setAttribute('value', '842a806765a8d12ece48e35c2b0340e1acc42c3e'); f.appendChild(s);f.submit();return false;" style="display:none"><span><span class="icon"></span>Unwatch</span></a>
        </li>
        
          
            <li class="for-notforked" style="display:none"><a href="/heuristicus/auv-localisation-ros/fork" class="minibutton btn-fork " id="fork_button" onclick="var f = document.createElement('form'); f.style.display = 'none'; this.parentNode.appendChild(f); f.method = 'POST'; f.action = this.href;var s = document.createElement('input'); s.setAttribute('type', 'hidden'); s.setAttribute('name', 'authenticity_token'); s.setAttribute('value', '842a806765a8d12ece48e35c2b0340e1acc42c3e'); f.appendChild(s);f.submit();return false;"><span><span class="icon"></span>Fork</span></a></li>
            <li class="for-hasfork" style="display:none"><a href="#" class="minibutton btn-fork " id="your_fork_button"><span><span class="icon"></span>Your Fork</span></a></li>
          

          <li id='pull_request_item' class='nspr' style='display:none'><a href="/heuristicus/auv-localisation-ros/pull/new/fe7c9224fbeba1411e2cd5b5fb0a00aa3a19f1df" class="minibutton btn-pull-request "><span><span class="icon"></span>Pull Request</span></a></li>
        
      
      
      <li class="repostats">
        <ul class="repo-stats">
          <li class="watchers"><a href="/heuristicus/auv-localisation-ros/watchers" title="Watchers" class="tooltipped downwards">1</a></li>
          <li class="forks"><a href="/heuristicus/auv-localisation-ros/network" title="Forks" class="tooltipped downwards">1</a></li>
        </ul>
      </li>
    </ul>

      </div>

        
  <ul class="tabs">
    <li><a href="/heuristicus/auv-localisation-ros/tree/" class="selected" highlight="repo_source">Source</a></li>
    <li><a href="/heuristicus/auv-localisation-ros/commits/" highlight="repo_commits">Commits</a></li>
    <li><a href="/heuristicus/auv-localisation-ros/network" highlight="repo_network">Network</a></li>
    <li><a href="/heuristicus/auv-localisation-ros/pulls" highlight="repo_pulls">Pull Requests (0)</a></li>

    
      <li><a href="/heuristicus/auv-localisation-ros/forkqueue" highlight="repo_fork_queue">Fork Queue</a></li>
    

    
      
      <li><a href="/heuristicus/auv-localisation-ros/issues" highlight="issues">Issues (0)</a></li>
    

                <li><a href="/heuristicus/auv-localisation-ros/wiki" highlight="repo_wiki">Wiki (0)</a></li>
        
    <li><a href="/heuristicus/auv-localisation-ros/graphs" highlight="repo_graphs">Graphs</a></li>

    

    <li class="contextswitch nochoices">
      <span class="toggle leftwards tooltipped" title="fe7c9224fbeba1411e2cd5b5fb0a00aa3a19f1df">
        <em>Tree:</em>
        <code>fe7c922</code>
      </span>
    </li>
  </ul>

  <div style="display:none" id="pl-description"><p><em class="placeholder">click here to add a description</em></p></div>
  <div style="display:none" id="pl-homepage"><p><em class="placeholder">click here to add a homepage</em></p></div>

  <div class="subnav-bar">
  
  <ul>
    <li>
      <a href="/heuristicus/auv-localisation-ros/branches" class="dropdown">Switch Branches (1)</a>
      <ul>
        
          
          
            <li><a href="/heuristicus/auv-localisation-ros/blob/master/nodes/sonar.py" data-name="master">master</a></li>
          
        
      </ul>
    </li>
    <li>
      <a href="#" class="dropdown defunct">Switch Tags (0)</a>
      
    </li>
    <li>
    
    <a href="/heuristicus/auv-localisation-ros/branches/master" class="manage">Branch List</a>
    
    </li>
  </ul>
</div>

  
  
  
  
  
  



        
    <div id="repo_details" class="metabox clearfix">
      <div id="repo_details_loader" class="metabox-loader" style="display:none">Sending Request&hellip;</div>

      
        <a href="/heuristicus/auv-localisation-ros/downloads" class="download-source" id="download_button" title="Download source, tagged packages and binaries."><span class="icon"></span>Downloads</a>
      

      <div id="repository_desc_wrapper">
      <div id="repository_description" rel="repository_description_edit">
        
          <p>ros code for experiments for auv-localisation project
            <span id="read_more" style="display:none">&mdash; <a href="#readme">Read more</a></span>
          </p>
        
      </div>

      <div id="repository_description_edit" style="display:none;" class="inline-edit">
        <form action="/heuristicus/auv-localisation-ros/admin/update" method="post"><div style="margin:0;padding:0"><input name="authenticity_token" type="hidden" value="842a806765a8d12ece48e35c2b0340e1acc42c3e" /></div>
          <input type="hidden" name="field" value="repository_description">
          <input type="text" class="textfield" name="value" value="ros code for experiments for auv-localisation project">
          <div class="form-actions">
            <button class="minibutton"><span>Save</span></button> &nbsp; <a href="#" class="cancel">Cancel</a>
          </div>
        </form>
      </div>

      
      <div class="repository-homepage" id="repository_homepage" rel="repository_homepage_edit">
        <p><a href="http://" rel="nofollow"></a></p>
      </div>

      <div id="repository_homepage_edit" style="display:none;" class="inline-edit">
        <form action="/heuristicus/auv-localisation-ros/admin/update" method="post"><div style="margin:0;padding:0"><input name="authenticity_token" type="hidden" value="842a806765a8d12ece48e35c2b0340e1acc42c3e" /></div>
          <input type="hidden" name="field" value="repository_homepage">
          <input type="text" class="textfield" name="value" value="">
          <div class="form-actions">
            <button class="minibutton"><span>Save</span></button> &nbsp; <a href="#" class="cancel">Cancel</a>
          </div>
        </form>
      </div>
      </div>
      <div class="rule "></div>
      <div class="url-box">
  

  <ul class="clone-urls">
    
      
        <li class="private_clone_url"><a href="git@github.com:heuristicus/auv-localisation-ros.git" data-permissions="Read+Write">SSH</a></li>
      
      <li class="http_clone_url"><a href="https://heuristicus@github.com/heuristicus/auv-localisation-ros.git" data-permissions="Read+Write">HTTP</a></li>
      <li class="public_clone_url"><a href="git://github.com/heuristicus/auv-localisation-ros.git" data-permissions="Read-Only">Git Read-Only</a></li>
    
    
  </ul>
  <input type="text" spellcheck="false" class="url-field" />
        <span style="display:none" id="clippy_709" class="url-box-clippy"></span>
      <span id="clippy_tooltip_clippy_709" class="clippy-tooltip tooltipped" title="copy to clipboard">
      <object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"
              width="14"
              height="14"
              class="clippy"
              id="clippy" >
      <param name="movie" value="https://a248.e.akamai.net/assets.github.com/flash/clippy.swf?v5"/>
      <param name="allowScriptAccess" value="always" />
      <param name="quality" value="high" />
      <param name="scale" value="noscale" />
      <param NAME="FlashVars" value="id=clippy_709&amp;copied=&amp;copyto=">
      <param name="bgcolor" value="#FFFFFF">
      <param name="wmode" value="opaque">
      <embed src="https://a248.e.akamai.net/assets.github.com/flash/clippy.swf?v5"
             width="14"
             height="14"
             name="clippy"
             quality="high"
             allowScriptAccess="always"
             type="application/x-shockwave-flash"
             pluginspage="http://www.macromedia.com/go/getflashplayer"
             FlashVars="id=clippy_709&amp;copied=&amp;copyto="
             bgcolor="#FFFFFF"
             wmode="opaque"
      />
      </object>
      </span>

  <p class="url-description"><strong>Read+Write</strong> access</p>
</div>

    </div>

    <div class="frame frame-center tree-finder" style="display:none">
      <div class="breadcrumb">
        <b><a href="/heuristicus/auv-localisation-ros">auv-localisation-ros</a></b> /
        <input class="tree-finder-input" type="text" name="query" autocomplete="off" spellcheck="false">
      </div>

      
        <div class="octotip">
          <p>
            <a href="/heuristicus/auv-localisation-ros/dismiss-tree-finder-help" class="dismiss js-dismiss-tree-list-help" title="Hide this notice forever">Dismiss</a>
            <strong>Octotip:</strong> You've activated the <em>file finder</em> by pressing <span class="kbd">t</span>
            Start typing to filter the file list. Use <span class="kbd badmono">↑</span> and <span class="kbd badmono">↓</span> to navigate,
            <span class="kbd">enter</span> to view files.
          </p>
        </div>
      

      <table class="tree-browser" cellpadding="0" cellspacing="0">
        <tr class="js-header"><th>&nbsp;</th><th>name</th></tr>
        <tr class="js-no-results no-results" style="display: none">
          <th colspan="2">No matching files</th>
        </tr>
        <tbody class="js-results-list">
        </tbody>
      </table>
    </div>

    <div id="jump-to-line" style="display:none">
      <h2>Jump to Line</h2>
      <form>
        <input class="textfield" type="text">
        <div class="full-button">
          <button type="submit" class="classy">
            <span>Go</span>
          </button>
        </div>
      </form>
    </div>


        

      </div><!-- /.pagehead -->

      

  







<script type="text/javascript">
  GitHub.downloadRepo = '/heuristicus/auv-localisation-ros/archives/fe7c9224fbeba1411e2cd5b5fb0a00aa3a19f1df'
  GitHub.revType = "SHA1"

  GitHub.repoName = "auv-localisation-ros"
  GitHub.controllerName = "blob"
  GitHub.actionName     = "show"
  GitHub.currentAction  = "blob#show"

  
    GitHub.loggedIn = true
    GitHub.hasWriteAccess = true
    GitHub.hasAdminAccess = true
    GitHub.watchingRepo = true
    GitHub.ignoredRepo = false
    GitHub.hasForkOfRepo = null
    GitHub.hasForked = true
  

  
</script>







  <div id="commit">
    <div class="group">
        
  <div class="envelope commit">
    <div class="human">
      
        <div class="message"><pre><a href="/heuristicus/auv-localisation-ros/commit/fe7c9224fbeba1411e2cd5b5fb0a00aa3a19f1df">more message types</a> </pre></div>
      

      <div class="actor">
        <div class="gravatar">
          
          <img src="https://secure.gravatar.com/avatar/986ae440573f3f1bc8e98fa45c48d211?s=140&d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png" alt="" width="30" height="30"  />
        </div>
        <div class="name"><a href="/heuristicus">heuristicus</a> <span>(author)</span></div>
        <div class="date">
          <time class="js-relative-date" datetime="2011-08-22T05:50:19-07:00" title="2011-08-22 05:50:19">August 22, 2011</time>
        </div>
      </div>

      

    </div>
    <div class="machine">
      <span>c</span>ommit&nbsp;&nbsp;<a href="/heuristicus/auv-localisation-ros/commit/fe7c9224fbeba1411e2cd5b5fb0a00aa3a19f1df" class="js-commit-link" data-key="c">fe7c9224fbeba1411e2c</a><br />
      <span>t</span>ree&nbsp;&nbsp;&nbsp;&nbsp;<a href="/heuristicus/auv-localisation-ros/tree/fe7c9224fbeba1411e2cd5b5fb0a00aa3a19f1df" class="js-tree-link" data-key="t">ac286ded79febea594ec</a><br />
      
        <span>p</span>arent&nbsp;
        
        <a href="/heuristicus/auv-localisation-ros/tree/9015709b5679763014c207f7f6ab461f3dbc7bd9" class="js-parent-link" data-key="p">9015709b5679763014c2</a>
      

    </div>
  </div>

    </div>
  </div>



  <div id="slider">

  

    <div class="breadcrumb" data-path="nodes/sonar.py/">
      <b><a href="/heuristicus/auv-localisation-ros/tree/fe7c9224fbeba1411e2cd5b5fb0a00aa3a19f1df">auv-localisation-ros</a></b> / <a href="/heuristicus/auv-localisation-ros/tree/fe7c9224fbeba1411e2cd5b5fb0a00aa3a19f1df/nodes">nodes</a> / sonar.py       <span style="display:none" id="clippy_4329" class="clippy">nodes/sonar.py</span>
      
      <object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"
              width="110"
              height="14"
              class="clippy"
              id="clippy" >
      <param name="movie" value="https://a248.e.akamai.net/assets.github.com/flash/clippy.swf?v5"/>
      <param name="allowScriptAccess" value="always" />
      <param name="quality" value="high" />
      <param name="scale" value="noscale" />
      <param NAME="FlashVars" value="id=clippy_4329&amp;copied=copied!&amp;copyto=copy to clipboard">
      <param name="bgcolor" value="#FFFFFF">
      <param name="wmode" value="opaque">
      <embed src="https://a248.e.akamai.net/assets.github.com/flash/clippy.swf?v5"
             width="110"
             height="14"
             name="clippy"
             quality="high"
             allowScriptAccess="always"
             type="application/x-shockwave-flash"
             pluginspage="http://www.macromedia.com/go/getflashplayer"
             FlashVars="id=clippy_4329&amp;copied=copied!&amp;copyto=copy to clipboard"
             bgcolor="#FFFFFF"
             wmode="opaque"
      />
      </object>
      

    </div>

    <div class="frames">
      <div class="frame frame-center" data-path="nodes/sonar.py/" data-permalink-url="/heuristicus/auv-localisation-ros/blob/fe7c9224fbeba1411e2cd5b5fb0a00aa3a19f1df/nodes/sonar.py">
        
          <ul class="big-actions">
            
            <li><a class="file-edit-link minibutton" href="/heuristicus/auv-localisation-ros/edit/__current_ref__/nodes/sonar.py"><span>Edit this file</span></a></li>
          </ul>
        

        <div id="files">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><img alt="Txt" height="16" src="https://a248.e.akamai.net/assets.github.com/images/icons/txt.png" width="16" /></span>
                <span class="mode" title="File Mode">100755</span>
                
                  <span>301 lines (242 sloc)</span>
                
                <span>10.879 kb</span>
              </div>
              <ul class="actions">
                <li><a href="/heuristicus/auv-localisation-ros/raw/fe7c9224fbeba1411e2cd5b5fb0a00aa3a19f1df/nodes/sonar.py" id="raw-url">raw</a></li>
                
                  <li><a href="/heuristicus/auv-localisation-ros/blame/fe7c9224fbeba1411e2cd5b5fb0a00aa3a19f1df/nodes/sonar.py">blame</a></li>
                
                <li><a href="/heuristicus/auv-localisation-ros/commits/fe7c9224fbeba1411e2cd5b5fb0a00aa3a19f1df/nodes/sonar.py">history</a></li>
              </ul>
            </div>
            
  <div class="data type-python">
    
      <table cellpadding="0" cellspacing="0" class="lines">
        <tr>
          <td>
            <pre class="line_numbers"><span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>
<span id="L259" rel="#L259">259</span>
<span id="L260" rel="#L260">260</span>
<span id="L261" rel="#L261">261</span>
<span id="L262" rel="#L262">262</span>
<span id="L263" rel="#L263">263</span>
<span id="L264" rel="#L264">264</span>
<span id="L265" rel="#L265">265</span>
<span id="L266" rel="#L266">266</span>
<span id="L267" rel="#L267">267</span>
<span id="L268" rel="#L268">268</span>
<span id="L269" rel="#L269">269</span>
<span id="L270" rel="#L270">270</span>
<span id="L271" rel="#L271">271</span>
<span id="L272" rel="#L272">272</span>
<span id="L273" rel="#L273">273</span>
<span id="L274" rel="#L274">274</span>
<span id="L275" rel="#L275">275</span>
<span id="L276" rel="#L276">276</span>
<span id="L277" rel="#L277">277</span>
<span id="L278" rel="#L278">278</span>
<span id="L279" rel="#L279">279</span>
<span id="L280" rel="#L280">280</span>
<span id="L281" rel="#L281">281</span>
<span id="L282" rel="#L282">282</span>
<span id="L283" rel="#L283">283</span>
<span id="L284" rel="#L284">284</span>
<span id="L285" rel="#L285">285</span>
<span id="L286" rel="#L286">286</span>
<span id="L287" rel="#L287">287</span>
<span id="L288" rel="#L288">288</span>
<span id="L289" rel="#L289">289</span>
<span id="L290" rel="#L290">290</span>
<span id="L291" rel="#L291">291</span>
<span id="L292" rel="#L292">292</span>
<span id="L293" rel="#L293">293</span>
<span id="L294" rel="#L294">294</span>
<span id="L295" rel="#L295">295</span>
<span id="L296" rel="#L296">296</span>
<span id="L297" rel="#L297">297</span>
<span id="L298" rel="#L298">298</span>
<span id="L299" rel="#L299">299</span>
<span id="L300" rel="#L300">300</span>
<span id="L301" rel="#L301">301</span>
</pre>
          </td>
          <td width="100%">
            
              
                <div class="highlight"><pre><div class='line' id='LC1'><span class="c">#!/usr/bin/python</span></div><div class='line' id='LC2'><span class="kn">import</span> <span class="nn">roslib</span><span class="p">;</span> <span class="n">roslib</span><span class="o">.</span><span class="n">load_manifest</span><span class="p">(</span><span class="s">&#39;loc_sonar&#39;</span><span class="p">)</span></div><div class='line' id='LC3'><span class="kn">import</span> <span class="nn">rospy</span></div><div class='line' id='LC4'><span class="kn">import</span> <span class="nn">sys</span></div><div class='line' id='LC5'><span class="kn">import</span> <span class="nn">serial</span></div><div class='line' id='LC6'><span class="kn">import</span> <span class="nn">time</span></div><div class='line' id='LC7'><span class="kn">import</span> <span class="nn">numpy</span></div><div class='line' id='LC8'><span class="kn">from</span> <span class="nn">std_msgs.msg</span> <span class="kn">import</span> <span class="n">String</span></div><div class='line' id='LC9'><span class="kn">from</span> <span class="nn">std_msgs.msg</span> <span class="kn">import</span> <span class="n">UInt16</span></div><div class='line' id='LC10'><span class="kn">from</span> <span class="nn">loc_sonar.msg</span> <span class="kn">import</span> <span class="n">sonar</span></div><div class='line' id='LC11'><span class="c">#from rospy_tutorials.msg import Floats</span></div><div class='line' id='LC12'><span class="kn">from</span> <span class="nn">rospy.numpy_msg</span> <span class="kn">import</span> <span class="n">numpy_msg</span></div><div class='line' id='LC13'><br/></div><div class='line' id='LC14'><span class="c">### to do:</span></div><div class='line' id='LC15'><span class="c">### make another version for N/E position estimate that takes in compass heading</span></div><div class='line' id='LC16'><span class="c">### set flags for various modes (wall following, position, scan all)</span></div><div class='line' id='LC17'><br/></div><div class='line' id='LC18'><span class="c">################################################################</span></div><div class='line' id='LC19'><span class="k">def</span> <span class="nf">sonarTalker</span><span class="p">():</span></div><div class='line' id='LC20'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># defines and sends the ping trigger (mtSendData) to the sonar. </span></div><div class='line' id='LC21'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">global</span> <span class="n">serialPort</span> </div><div class='line' id='LC22'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#trigger = [64, 48, 48, 48, 67, 12, 0, 255, 2, 7, 25, 128, 255, 0, 0, 0, 0, 10]</span></div><div class='line' id='LC23'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC24'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># construct message using parameters/constants</span></div><div class='line' id='LC25'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">AsciiBlock</span> <span class="o">=</span> <span class="p">[</span><span class="mi">64</span><span class="p">,</span> <span class="mi">48</span><span class="p">,</span> <span class="mi">48</span><span class="p">,</span> <span class="mi">48</span><span class="p">,</span> <span class="mi">67</span><span class="p">]</span> <span class="c"># @000C - ASCII header to msg</span></div><div class='line' id='LC26'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">hexLength</span> <span class="o">=</span> <span class="p">[</span><span class="mi">12</span><span class="p">,</span> <span class="mi">0</span><span class="p">]</span> <span class="c"># Length of block in 2 bit int</span></div><div class='line' id='LC27'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">SID</span> <span class="o">=</span> <span class="n">rospy</span><span class="o">.</span><span class="n">get_param</span><span class="p">(</span><span class="s">&quot;/SID&quot;</span><span class="p">)</span></div><div class='line' id='LC28'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">DID</span> <span class="o">=</span> <span class="n">rospy</span><span class="o">.</span><span class="n">get_param</span><span class="p">(</span><span class="s">&quot;/DID&quot;</span><span class="p">)</span></div><div class='line' id='LC29'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">count</span> <span class="o">=</span> <span class="mi">7</span> <span class="c"># Number of bytes following count byte - excluding LF character </span></div><div class='line' id='LC30'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">msgNum</span> <span class="o">=</span> <span class="mi">25</span> <span class="c"># Msg identification number</span></div><div class='line' id='LC31'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">msgSeq</span> <span class="o">=</span> <span class="n">rospy</span><span class="o">.</span><span class="n">get_param</span><span class="p">(</span><span class="s">&quot;/msgSeq&quot;</span><span class="p">)</span></div><div class='line' id='LC32'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Node</span> <span class="o">=</span> <span class="n">rospy</span><span class="o">.</span><span class="n">get_param</span><span class="p">(</span><span class="s">&quot;/Node&quot;</span><span class="p">)</span></div><div class='line' id='LC33'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">currentTime</span> <span class="o">=</span> <span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">]</span> <span class="c"># current time for sonar, not required for imaging as signals not time stamped</span></div><div class='line' id='LC34'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LF</span> <span class="o">=</span> <span class="mi">10</span></div><div class='line' id='LC35'><br/></div><div class='line' id='LC36'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">mtSendData</span> <span class="o">=</span> <span class="n">AsciiBlock</span> <span class="o">+</span> <span class="n">hexLength</span> <span class="o">+</span> <span class="p">[</span><span class="n">SID</span><span class="p">,</span> <span class="n">DID</span><span class="p">,</span> <span class="n">count</span><span class="p">,</span> <span class="n">msgNum</span><span class="p">,</span> <span class="n">msgSeq</span><span class="p">,</span> <span class="n">Node</span><span class="p">]</span> <span class="o">+</span> <span class="n">currentTime</span> <span class="o">+</span> <span class="p">[</span><span class="n">LF</span><span class="p">]</span></div><div class='line' id='LC37'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">mtSendData</span> <span class="o">=</span> <span class="s">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="nb">chr</span><span class="p">(</span><span class="n">char</span><span class="p">)</span> <span class="k">for</span> <span class="n">char</span> <span class="ow">in</span> <span class="n">mtSendData</span><span class="p">[:]])</span></div><div class='line' id='LC38'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">serialPort</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">mtSendData</span><span class="p">)</span></div><div class='line' id='LC39'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># print:</span></div><div class='line' id='LC40'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;Sending ping trigger to sonar - mtSendData:&quot;</span></div><div class='line' id='LC41'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="n">mtSendData</span></div><div class='line' id='LC42'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;--------&quot;</span></div><div class='line' id='LC43'><br/></div><div class='line' id='LC44'><br/></div><div class='line' id='LC45'><span class="c">################################################################</span></div><div class='line' id='LC46'><span class="k">def</span> <span class="nf">sonarListener</span><span class="p">():</span></div><div class='line' id='LC47'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># reads in the ping reply from the sonar (mtHeadData), determines the message type and publishes the ping data if applicable</span></div><div class='line' id='LC48'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">global</span> <span class="n">serialPort</span></div><div class='line' id='LC49'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;No. of chars in buffer:&quot;</span></div><div class='line' id='LC50'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="n">serialPort</span><span class="o">.</span><span class="n">inWaiting</span><span class="p">()</span></div><div class='line' id='LC51'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">serialPort</span><span class="o">.</span><span class="n">inWaiting</span><span class="p">()</span> <span class="o">&gt;</span> <span class="mi">12</span><span class="p">:</span></div><div class='line' id='LC52'>	<span class="c"># read message header, first 13 bytes (as specified in SonarPing.m)</span></div><div class='line' id='LC53'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">headerData</span> <span class="o">=</span> <span class="n">serialPort</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="mi">13</span><span class="p">)</span></div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#print headerData</span></div><div class='line' id='LC55'>	<span class="n">headerData</span> <span class="o">=</span> <span class="n">numpy</span><span class="o">.</span><span class="n">fromstring</span><span class="p">(</span><span class="n">headerData</span><span class="p">,</span> <span class="n">dtype</span><span class="o">=</span><span class="n">numpy</span><span class="o">.</span><span class="n">uint8</span><span class="p">)</span>       </div><div class='line' id='LC56'>	<span class="c"># print:</span></div><div class='line' id='LC57'>	<span class="k">print</span> <span class="s">&quot;Data from sonar: mtHeadData:&quot;</span></div><div class='line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="n">headerData</span></div><div class='line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;--------&quot;</span></div><div class='line' id='LC60'><br/></div><div class='line' id='LC61'>	<span class="k">if</span> <span class="n">headerData</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="mi">64</span><span class="p">:</span></div><div class='line' id='LC62'>	    <span class="n">msgType</span> <span class="o">=</span> <span class="n">headerData</span><span class="p">[</span><span class="mi">10</span><span class="p">]</span></div><div class='line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;Message type:&quot;</span></div><div class='line' id='LC64'>	    <span class="k">print</span> <span class="n">msgType</span></div><div class='line' id='LC65'><br/></div><div class='line' id='LC66'>	    <span class="c"># From sonarPing.m: get the length of the rest of the data</span></div><div class='line' id='LC67'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#    calulate from mtAlive 22 bytes in total, header[5:7] = 16 bytes and we load in 13 bytes initially</span></div><div class='line' id='LC68'>	    <span class="c">#    thus number to remove = 16 - (22-13) = 7</span></div><div class='line' id='LC69'>	    <span class="c"># headerData[5]+headerData[6]*256 = simulating Matlab typecast function - converting 2 uint8s to 1 uint16  </span></div><div class='line' id='LC70'>	    <span class="n">msgLength</span> <span class="o">=</span> <span class="p">(</span><span class="n">headerData</span><span class="p">[</span><span class="mi">5</span><span class="p">]</span><span class="o">+</span><span class="p">(</span><span class="n">headerData</span><span class="p">[</span><span class="mi">6</span><span class="p">]</span><span class="o">*</span><span class="mi">256</span><span class="p">))</span><span class="o">-</span><span class="mi">7</span></div><div class='line' id='LC71'>	    <span class="k">print</span> <span class="n">msgLength</span></div><div class='line' id='LC72'>	    <span class="k">print</span> <span class="n">serialPort</span><span class="o">.</span><span class="n">inWaiting</span><span class="p">()</span></div><div class='line' id='LC73'><br/></div><div class='line' id='LC74'>	    <span class="n">timeOut</span> <span class="o">=</span> <span class="mf">0.1</span><span class="o">/</span><span class="p">(</span><span class="mi">24</span><span class="o">*</span><span class="mi">3600</span><span class="p">)</span></div><div class='line' id='LC75'>	    <span class="n">startTime</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span></div><div class='line' id='LC76'><br/></div><div class='line' id='LC77'>	    <span class="c"># makes sure full message has been read - may not be needed, but present in sonarPing.m</span></div><div class='line' id='LC78'>	    <span class="k">while</span> <span class="n">serialPort</span><span class="o">.</span><span class="n">inWaiting</span><span class="p">()</span><span class="o">&lt;</span><span class="n">msgLength</span><span class="p">:</span></div><div class='line' id='LC79'>		<span class="k">print</span> <span class="s">&#39;looping&#39;</span></div><div class='line' id='LC80'>		<span class="k">if</span> <span class="n">startTime</span><span class="o">+</span><span class="n">timeOut</span> <span class="o">&lt;</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">():</span></div><div class='line' id='LC81'>		    <span class="k">print</span> <span class="s">&quot;Timeout error&quot;</span></div><div class='line' id='LC82'>		    <span class="k">return</span></div><div class='line' id='LC83'><br/></div><div class='line' id='LC84'>&nbsp;	    <span class="n">msgData</span> <span class="o">=</span> <span class="n">serialPort</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="n">serialPort</span><span class="o">.</span><span class="n">inWaiting</span><span class="p">())</span> <span class="c"># read rest of message</span></div><div class='line' id='LC85'>	    <span class="n">msgData</span> <span class="o">=</span> <span class="n">numpy</span><span class="o">.</span><span class="n">fromstring</span><span class="p">(</span><span class="n">msgData</span><span class="p">,</span> <span class="n">dtype</span><span class="o">=</span><span class="n">numpy</span><span class="o">.</span><span class="n">uint8</span><span class="p">)</span>   </div><div class='line' id='LC86'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="n">msgData</span></div><div class='line' id='LC87'>&nbsp;&nbsp;&nbsp;	   </div><div class='line' id='LC88'>	    <span class="c"># if msgData does not end in LF character - could I do this without converting to a numpy array?</span></div><div class='line' id='LC89'>	    <span class="k">if</span> <span class="n">msgData</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">!=</span> <span class="mi">10</span><span class="p">:</span></div><div class='line' id='LC90'>	 	<span class="k">print</span> <span class="s">&quot;Message error: missing LF character&quot;</span> </div><div class='line' id='LC91'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">serialPort</span><span class="o">.</span><span class="n">flushInput</span><span class="p">()</span></div><div class='line' id='LC92'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span></div><div class='line' id='LC93'><br/></div><div class='line' id='LC94'>	    <span class="k">if</span> <span class="n">msgType</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span></div><div class='line' id='LC95'>		<span class="k">print</span> <span class="s">&quot;mtVersionData&quot;</span></div><div class='line' id='LC96'>		<span class="c"># mtVersionData</span></div><div class='line' id='LC97'>	    <span class="k">elif</span> <span class="n">msgType</span> <span class="o">==</span> <span class="mi">2</span><span class="p">:</span></div><div class='line' id='LC98'>		<span class="k">print</span> <span class="s">&quot;mtHeadData&quot;</span></div><div class='line' id='LC99'>		<span class="c">#pingPwr = msgData[31:-1]</span></div><div class='line' id='LC100'>		<span class="c">#print pingPwr</span></div><div class='line' id='LC101'>		<span class="n">transBearing</span> <span class="o">=</span> <span class="n">msgData</span><span class="p">[</span><span class="mi">27</span><span class="p">]</span><span class="o">+</span><span class="p">(</span><span class="n">msgData</span><span class="p">[</span><span class="mi">28</span><span class="p">]</span><span class="o">*</span><span class="mi">256</span><span class="p">)</span></div><div class='line' id='LC102'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC103'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#TEST LINE:</span></div><div class='line' id='LC104'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">msgData</span> <span class="o">=</span> <span class="n">numpy</span><span class="o">.</span><span class="n">concatenate</span><span class="p">((</span><span class="n">headerData</span><span class="p">,</span><span class="n">msgData</span><span class="p">))</span></div><div class='line' id='LC105'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC106'>		<span class="c">#print msgData[28]</span></div><div class='line' id='LC107'>		<span class="k">print</span> <span class="n">transBearing</span></div><div class='line' id='LC108'>		<span class="k">print</span> <span class="s">&quot;Publishing....&quot;</span></div><div class='line' id='LC109'><br/></div><div class='line' id='LC110'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		<span class="n">pub</span> <span class="o">=</span> <span class="n">rospy</span><span class="o">.</span><span class="n">Publisher</span><span class="p">(</span><span class="s">&#39;sonar_output&#39;</span><span class="p">,</span> <span class="n">String</span><span class="p">)</span></div><div class='line' id='LC111'>&nbsp;		<span class="n">msgData</span> <span class="o">=</span> <span class="s">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="nb">chr</span><span class="p">(</span><span class="n">char</span><span class="p">)</span> <span class="k">for</span> <span class="n">char</span> <span class="ow">in</span> <span class="n">msgData</span><span class="p">[:]])</span></div><div class='line' id='LC112'>		<span class="n">pub</span><span class="o">.</span><span class="n">publish</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">msgData</span><span class="p">))</span></div><div class='line' id='LC113'><br/></div><div class='line' id='LC114'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">msgType</span> <span class="o">==</span> <span class="mi">4</span><span class="p">:</span></div><div class='line' id='LC115'>		<span class="k">print</span> <span class="s">&quot;mtAlive&quot;</span></div><div class='line' id='LC116'>		<span class="k">return</span> <span class="mi">4</span></div><div class='line' id='LC117'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC118'>		<span class="k">print</span> <span class="s">&quot;Error: Unknown message type&quot;</span></div><div class='line' id='LC119'><br/></div><div class='line' id='LC120'><br/></div><div class='line' id='LC121'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC122'>&nbsp;	    <span class="k">print</span> <span class="s">&quot;Message error: @&quot;</span> </div><div class='line' id='LC123'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">serialPort</span><span class="o">.</span><span class="n">flushInput</span><span class="p">()</span></div><div class='line' id='LC124'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span></div><div class='line' id='LC125'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC126'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC127'><span class="c">################################################################    </span></div><div class='line' id='LC128'><span class="k">def</span> <span class="nf">setupSonar</span><span class="p">():</span></div><div class='line' id='LC129'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># sends the setup command (mtHeadCommand) to the sonar - NEEDS EDITING TO ADD CALLBACK FUNCTION AND UPDATE FROM PARAMETER DATABASE</span></div><div class='line' id='LC130'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rospy</span><span class="o">.</span><span class="n">init_node</span><span class="p">(</span><span class="s">&#39;sonar&#39;</span><span class="p">)</span></div><div class='line' id='LC131'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">global</span> <span class="n">serialPort</span> </div><div class='line' id='LC132'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># settings for Micron Sonar</span></div><div class='line' id='LC133'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">serialPort</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">Serial</span><span class="p">(</span><span class="n">port</span><span class="o">=</span><span class="s">&#39;/dev/ttyUSB0&#39;</span><span class="p">,</span> <span class="n">baudrate</span><span class="o">=</span><span class="s">&#39;57600 &#39;</span><span class="p">)</span></div><div class='line' id='LC134'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">serialPort</span><span class="o">.</span><span class="n">bytesize</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">EIGHTBITS</span></div><div class='line' id='LC135'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">serialPort</span><span class="o">.</span><span class="n">stopbits</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">STOPBITS_ONE</span></div><div class='line' id='LC136'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">serialPort</span><span class="o">.</span><span class="n">parity</span> <span class="o">=</span> <span class="n">serial</span><span class="o">.</span><span class="n">PARITY_NONE</span></div><div class='line' id='LC137'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;Setup sonar: mtHeadCommand:&quot;</span></div><div class='line' id='LC138'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="n">serialPort</span><span class="o">.</span><span class="n">portstr</span></div><div class='line' id='LC139'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="n">serialPort</span><span class="o">.</span><span class="n">isOpen</span><span class="p">()</span></div><div class='line' id='LC140'><br/></div><div class='line' id='LC141'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#setupData = [64, 48, 48, 51, 67, 60, 0, 255, 2, 55, 19, 128, 255, 1, 1, 35, 11, 102, 102, 102, 5, 102, 102, 102, 5, 112, 61, 10, 9, 112, 61, 10, 9, 40, 0, 60, 0, 128, 12, 128, 12, 210, 0, 84, 84, 125, 0, 125, 0, 25, 64, 208, 0, 144, 1, 244, 1, 100, 0, 64, 6, 1, 0, 0, 0, 10]</span></div><div class='line' id='LC142'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">flag</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC143'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">while</span><span class="p">(</span><span class="n">flag</span> <span class="o">!=</span><span class="mi">4</span><span class="p">):</span></div><div class='line' id='LC144'>&nbsp;&nbsp;&nbsp;&nbsp;	<span class="n">setupData</span> <span class="o">=</span> <span class="n">get_mtHeadCommand</span><span class="p">()</span></div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;	<span class="n">serialPort</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">setupData</span><span class="p">)</span></div><div class='line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mf">0.1</span><span class="p">)</span></div><div class='line' id='LC147'><br/></div><div class='line' id='LC148'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&#39;still waiting for mtAlive....&#39;</span></div><div class='line' id='LC149'>&nbsp;&nbsp;&nbsp;&nbsp;	<span class="n">flag</span> <span class="o">=</span> <span class="n">sonarListener</span><span class="p">()</span></div><div class='line' id='LC150'><br/></div><div class='line' id='LC151'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">setupData</span> <span class="o">=</span> <span class="n">get_mtHeadCommand</span><span class="p">()</span></div><div class='line' id='LC152'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="n">setupData</span></div><div class='line' id='LC153'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;--------&quot;</span></div><div class='line' id='LC154'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">serialPort</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">setupData</span><span class="p">)</span></div><div class='line' id='LC155'><br/></div><div class='line' id='LC156'><br/></div><div class='line' id='LC157'><span class="c">################################################################</span></div><div class='line' id='LC158'><span class="k">def</span> <span class="nf">get_mtHeadCommand</span><span class="p">():</span></div><div class='line' id='LC159'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># hard-coded as specific to this message:</span></div><div class='line' id='LC160'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">AsciiBlock</span><span class="o">=</span> <span class="p">[</span><span class="mi">64</span><span class="p">,</span> <span class="mi">48</span><span class="p">,</span> <span class="mi">48</span><span class="p">,</span> <span class="mi">51</span><span class="p">,</span> <span class="mi">67</span><span class="p">]</span> <span class="c"># @003C - ASCII header to msg </span></div><div class='line' id='LC161'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">hexLength</span> <span class="o">=</span> <span class="p">[</span><span class="mi">60</span><span class="p">,</span> <span class="mi">0</span><span class="p">]</span> <span class="c"># Length of block in 2 bit int</span></div><div class='line' id='LC162'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">count</span> <span class="o">=</span> <span class="mi">55</span> 		<span class="c"># Number of bytes following count byte - excluding LF character</span></div><div class='line' id='LC163'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">msgNum</span> <span class="o">=</span> <span class="mi">19</span> 	<span class="c"># Msg identification number</span></div><div class='line' id='LC164'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC165'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># construct message using parameters</span></div><div class='line' id='LC166'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">SID</span> <span class="o">=</span> <span class="n">rospy</span><span class="o">.</span><span class="n">get_param</span><span class="p">(</span><span class="s">&quot;/SID&quot;</span><span class="p">)</span></div><div class='line' id='LC167'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">DID</span> <span class="o">=</span> <span class="n">rospy</span><span class="o">.</span><span class="n">get_param</span><span class="p">(</span><span class="s">&quot;/DID&quot;</span><span class="p">)</span></div><div class='line' id='LC168'><br/></div><div class='line' id='LC169'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">headType</span> <span class="o">=</span> <span class="n">rospy</span><span class="o">.</span><span class="n">get_param</span><span class="p">(</span><span class="s">&quot;/headType&quot;</span><span class="p">)</span></div><div class='line' id='LC170'><br/></div><div class='line' id='LC171'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">msgSeq</span> <span class="o">=</span> <span class="n">rospy</span><span class="o">.</span><span class="n">get_param</span><span class="p">(</span><span class="s">&quot;/msgSeq&quot;</span><span class="p">)</span></div><div class='line' id='LC172'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Node</span> <span class="o">=</span> <span class="n">rospy</span><span class="o">.</span><span class="n">get_param</span><span class="p">(</span><span class="s">&quot;/Node&quot;</span><span class="p">)</span></div><div class='line' id='LC173'>&nbsp;&nbsp;</div><div class='line' id='LC174'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">HdCtrl1</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">rospy</span><span class="o">.</span><span class="n">get_param</span><span class="p">(</span><span class="s">&quot;/HdCtrl1&quot;</span><span class="p">),</span><span class="mi">2</span><span class="p">)</span></div><div class='line' id='LC175'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">HdCtrl2</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">rospy</span><span class="o">.</span><span class="n">get_param</span><span class="p">(</span><span class="s">&quot;/HdCtrl2&quot;</span><span class="p">),</span><span class="mi">2</span><span class="p">)</span></div><div class='line' id='LC176'><br/></div><div class='line' id='LC177'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">DstHead</span> <span class="o">=</span> <span class="n">rospy</span><span class="o">.</span><span class="n">get_param</span><span class="p">(</span><span class="s">&quot;/DstHead&quot;</span><span class="p">)</span></div><div class='line' id='LC178'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">TXNChan</span> <span class="o">=</span> <span class="p">[</span><span class="mi">102</span><span class="p">,</span> <span class="mi">102</span><span class="p">,</span> <span class="mi">102</span><span class="p">,</span> <span class="mi">5</span><span class="p">]</span> <span class="c"># Hard coded as not used by DST sonars</span></div><div class='line' id='LC179'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">RXNChan</span> <span class="o">=</span> <span class="p">[</span><span class="mi">112</span><span class="p">,</span> <span class="mi">61</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">9</span><span class="p">]</span> <span class="c"># Hard coded as not used by DST sonars</span></div><div class='line' id='LC180'><br/></div><div class='line' id='LC181'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">txPulseLength</span> <span class="o">=</span> <span class="p">[</span><span class="mi">40</span><span class="p">,</span> <span class="mi">0</span><span class="p">]</span> <span class="c"># Hard coded as not used by DST sonars</span></div><div class='line' id='LC182'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rangeScale</span> <span class="o">=</span> <span class="p">[</span><span class="mi">60</span><span class="p">,</span> <span class="mi">0</span><span class="p">]</span> <span class="c"># Hard coded as not used by sonar head</span></div><div class='line' id='LC183'><br/></div><div class='line' id='LC184'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># CURRENTLY DESIGNED TO POINT AND PING (LIKE SONARPING.M)</span></div><div class='line' id='LC185'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#LLim = uint16_to_uint8(rospy.get_param(&quot;/LLim&quot;))  # anti-clockwise scan limit in 1/16th of a gradian</span></div><div class='line' id='LC186'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#RLim = uint16_to_uint8(rospy.get_param(&quot;/RLim&quot;))  # clockwise scan limit in 1/16th of a gradian</span></div><div class='line' id='LC187'>&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC188'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LLim</span> <span class="o">=</span> <span class="n">rospy</span><span class="o">.</span><span class="n">get_param</span><span class="p">(</span><span class="s">&quot;/LLim&quot;</span><span class="p">)</span>  <span class="c"># convert anti-clockwise scan limit from degrees to 16ths of a gradian (+90 accounts for sonar mounting)</span></div><div class='line' id='LC189'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LLim</span> <span class="o">=</span> <span class="p">(</span><span class="n">LLim</span>   <span class="p">)</span><span class="o">%</span><span class="mi">360</span></div><div class='line' id='LC190'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LLim</span> <span class="o">=</span> <span class="n">LLim</span><span class="o">/</span><span class="mf">360.0</span> <span class="o">*</span> <span class="mi">6400</span></div><div class='line' id='LC191'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="n">LLim</span></div><div class='line' id='LC192'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">RLim</span> <span class="o">=</span> <span class="n">rospy</span><span class="o">.</span><span class="n">get_param</span><span class="p">(</span><span class="s">&quot;/RLim&quot;</span><span class="p">)</span>   <span class="c"># clockwise scan limit from degrees to 16ths of a gradian (+90 accounts for sonar mounting)</span></div><div class='line' id='LC193'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">RLim</span> <span class="o">=</span> <span class="p">(</span><span class="n">RLim</span>   <span class="p">)</span><span class="o">%</span><span class="mi">360</span></div><div class='line' id='LC194'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">RLim</span> <span class="o">=</span> <span class="n">RLim</span><span class="o">/</span><span class="mf">360.0</span> <span class="o">*</span> <span class="mi">6400</span></div><div class='line' id='LC195'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="n">RLim</span></div><div class='line' id='LC196'><br/></div><div class='line' id='LC197'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LLim</span> <span class="o">=</span> <span class="n">uint16_to_uint8</span><span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="n">LLim</span><span class="p">))</span></div><div class='line' id='LC198'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">RLim</span> <span class="o">=</span> <span class="n">uint16_to_uint8</span><span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="n">RLim</span><span class="p">))</span></div><div class='line' id='LC199'><br/></div><div class='line' id='LC200'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="n">LLim</span> </div><div class='line' id='LC201'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="n">RLim</span></div><div class='line' id='LC202'><br/></div><div class='line' id='LC203'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ADSpan</span> <span class="o">=</span> <span class="n">rospy</span><span class="o">.</span><span class="n">get_param</span><span class="p">(</span><span class="s">&quot;/ADSpan&quot;</span><span class="p">)</span></div><div class='line' id='LC204'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ADLow</span> <span class="o">=</span> <span class="n">rospy</span><span class="o">.</span><span class="n">get_param</span><span class="p">(</span><span class="s">&quot;/ADLow&quot;</span><span class="p">)</span></div><div class='line' id='LC205'><br/></div><div class='line' id='LC206'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">IGainB1</span> <span class="o">=</span> <span class="n">rospy</span><span class="o">.</span><span class="n">get_param</span><span class="p">(</span><span class="s">&quot;/IGainB1&quot;</span><span class="p">)</span></div><div class='line' id='LC207'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">IGainB2</span> <span class="o">=</span> <span class="n">rospy</span><span class="o">.</span><span class="n">get_param</span><span class="p">(</span><span class="s">&quot;/IGainB2&quot;</span><span class="p">)</span></div><div class='line' id='LC208'><br/></div><div class='line' id='LC209'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Slope</span> <span class="o">=</span> <span class="p">[</span><span class="mi">125</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">125</span><span class="p">,</span> <span class="mi">0</span><span class="p">]</span> <span class="c"># Hard coded as not used by DST sonars</span></div><div class='line' id='LC210'><br/></div><div class='line' id='LC211'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">moTime</span> <span class="o">=</span> <span class="n">rospy</span><span class="o">.</span><span class="n">get_param</span><span class="p">(</span><span class="s">&quot;/moTime&quot;</span><span class="p">)</span></div><div class='line' id='LC212'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">step</span> <span class="o">=</span> <span class="n">rospy</span><span class="o">.</span><span class="n">get_param</span><span class="p">(</span><span class="s">&quot;/step&quot;</span><span class="p">)</span></div><div class='line' id='LC213'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="n">step</span></div><div class='line' id='LC214'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC215'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">NBins</span> <span class="o">=</span> <span class="n">rospy</span><span class="o">.</span><span class="n">get_param</span><span class="p">(</span><span class="s">&quot;/NBins&quot;</span><span class="p">)</span></div><div class='line' id='LC216'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Range</span> <span class="o">=</span> <span class="n">rospy</span><span class="o">.</span><span class="n">get_param</span><span class="p">(</span><span class="s">&quot;/Range&quot;</span><span class="p">)</span></div><div class='line' id='LC217'>&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC218'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ADInterval</span> <span class="o">=</span> <span class="n">uint16_to_uint8</span><span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="nb">round</span><span class="p">((((</span><span class="n">Range</span><span class="o">*</span><span class="mi">2</span><span class="p">)</span><span class="o">/</span><span class="mf">1500.0</span><span class="p">)</span><span class="o">/</span><span class="n">NBins</span><span class="p">)</span><span class="o">/</span><span class="mf">0.000000640</span><span class="p">,</span><span class="mi">0</span><span class="p">)))</span> </div><div class='line' id='LC219'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rospy</span><span class="o">.</span><span class="n">set_param</span><span class="p">(</span><span class="s">&quot;/ADInterval&quot;</span><span class="p">,</span> <span class="n">ADInterval</span><span class="p">)</span> <span class="c">#updates ADInterval to parameter server for user in sonar_detect_obstacle</span></div><div class='line' id='LC220'><br/></div><div class='line' id='LC221'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">NBins</span> <span class="o">=</span> <span class="n">uint16_to_uint8</span><span class="p">(</span><span class="n">NBins</span><span class="p">)</span></div><div class='line' id='LC222'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC223'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">MaxADBuf</span> <span class="o">=</span> <span class="n">uint16_to_uint8</span><span class="p">(</span><span class="n">rospy</span><span class="o">.</span><span class="n">get_param</span><span class="p">(</span><span class="s">&quot;/MaxADBuf&quot;</span><span class="p">))</span></div><div class='line' id='LC224'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Lockout</span> <span class="o">=</span> <span class="n">uint16_to_uint8</span><span class="p">(</span><span class="n">rospy</span><span class="o">.</span><span class="n">get_param</span><span class="p">(</span><span class="s">&quot;/Lockout&quot;</span><span class="p">))</span></div><div class='line' id='LC225'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">MinorAxis</span> <span class="o">=</span> <span class="n">uint16_to_uint8</span><span class="p">(</span><span class="n">rospy</span><span class="o">.</span><span class="n">get_param</span><span class="p">(</span><span class="s">&quot;/MinorAxis&quot;</span><span class="p">))</span></div><div class='line' id='LC226'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">MajorAxis</span> <span class="o">=</span> <span class="n">rospy</span><span class="o">.</span><span class="n">get_param</span><span class="p">(</span><span class="s">&quot;/MajorAxis&quot;</span><span class="p">)</span></div><div class='line' id='LC227'><br/></div><div class='line' id='LC228'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Ctl2</span> <span class="o">=</span> <span class="n">rospy</span><span class="o">.</span><span class="n">get_param</span><span class="p">(</span><span class="s">&quot;/Ctl2&quot;</span><span class="p">)</span></div><div class='line' id='LC229'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ScanZ</span> <span class="o">=</span> <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">]</span> <span class="c"># Hard coded as always set to 0</span></div><div class='line' id='LC230'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LF</span> <span class="o">=</span> <span class="mi">10</span> <span class="c"># Hard coded as always set to 10</span></div><div class='line' id='LC231'><br/></div><div class='line' id='LC232'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># constructs mtHeadCommand to send to sonar</span></div><div class='line' id='LC233'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">mtHeadCommand</span> <span class="o">=</span> <span class="n">AsciiBlock</span> <span class="o">+</span> <span class="n">hexLength</span> <span class="o">+</span> <span class="p">[</span><span class="n">SID</span><span class="p">,</span> <span class="n">DID</span><span class="p">,</span> <span class="n">count</span><span class="p">,</span> <span class="n">msgNum</span><span class="p">,</span> <span class="n">msgSeq</span><span class="p">,</span> <span class="n">Node</span><span class="p">,</span> <span class="n">headType</span><span class="p">,</span> <span class="n">HdCtrl1</span><span class="p">,</span> <span class="n">HdCtrl2</span><span class="p">,</span> <span class="n">DstHead</span><span class="p">]</span> <span class="o">+</span> <span class="n">TXNChan</span> <span class="o">+</span> <span class="n">TXNChan</span> <span class="o">+</span> <span class="n">RXNChan</span> <span class="o">+</span> <span class="n">RXNChan</span> <span class="o">+</span> <span class="n">txPulseLength</span> <span class="o">+</span> <span class="n">rangeScale</span> <span class="o">+</span> <span class="n">LLim</span> <span class="o">+</span> <span class="n">RLim</span> <span class="o">+</span><span class="p">[</span><span class="n">ADSpan</span><span class="p">,</span> <span class="n">ADLow</span><span class="p">,</span> <span class="n">IGainB1</span><span class="p">,</span> <span class="n">IGainB2</span><span class="p">]</span> <span class="o">+</span> <span class="n">Slope</span> <span class="o">+</span> <span class="p">[</span><span class="n">moTime</span><span class="p">,</span> <span class="n">step</span><span class="p">]</span> <span class="o">+</span> <span class="n">ADInterval</span><span class="o">+</span> <span class="n">NBins</span> <span class="o">+</span> <span class="n">MaxADBuf</span> <span class="o">+</span> <span class="n">Lockout</span> <span class="o">+</span> <span class="n">MinorAxis</span> <span class="o">+</span> <span class="p">[</span><span class="n">MajorAxis</span><span class="p">,</span> <span class="n">Ctl2</span><span class="p">]</span> <span class="o">+</span> <span class="n">ScanZ</span> <span class="o">+</span> <span class="p">[</span><span class="n">LF</span><span class="p">]</span></div><div class='line' id='LC234'><br/></div><div class='line' id='LC235'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">mtHeadCommand</span> <span class="o">=</span> <span class="s">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="nb">chr</span><span class="p">(</span><span class="n">char</span><span class="p">)</span> <span class="k">for</span> <span class="n">char</span> <span class="ow">in</span> <span class="n">mtHeadCommand</span><span class="p">[:]])</span></div><div class='line' id='LC236'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">mtHeadCommand</span></div><div class='line' id='LC237'><br/></div><div class='line' id='LC238'><span class="c">################################################################</span></div><div class='line' id='LC239'><span class="k">def</span> <span class="nf">uint16_to_uint8</span><span class="p">(</span><span class="n">input16</span><span class="p">):</span></div><div class='line' id='LC240'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#converts a single uint16 to two uint8s</span></div><div class='line' id='LC241'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">B1</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">numpy</span><span class="o">.</span><span class="n">uint8</span><span class="p">(</span><span class="n">input16</span><span class="p">))</span></div><div class='line' id='LC242'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">B2</span> <span class="o">=</span> <span class="p">(</span><span class="n">input16</span><span class="o">-</span><span class="n">B1</span><span class="p">)</span><span class="o">/</span><span class="mi">256</span></div><div class='line' id='LC243'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">output8</span> <span class="o">=</span> <span class="p">[</span><span class="n">B1</span><span class="p">,</span> <span class="n">B2</span><span class="p">]</span></div><div class='line' id='LC244'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">output8</span></div><div class='line' id='LC245'><br/></div><div class='line' id='LC246'><span class="c">################################################################</span></div><div class='line' id='LC247'><span class="k">def</span> <span class="nf">callback</span><span class="p">(</span><span class="n">data</span><span class="p">):</span></div><div class='line' id='LC248'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&quot;UPDATE CALLBACK TRIGGERED!!!&quot;</span></div><div class='line' id='LC249'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">global</span> <span class="n">updateFlag</span></div><div class='line' id='LC250'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">updateFlag</span> <span class="o">=</span> <span class="mi">1</span></div><div class='line' id='LC251'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#rospy.set_param(&quot;/heading&quot;, int(data.data))</span></div><div class='line' id='LC252'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rospy</span><span class="o">.</span><span class="n">set_param</span><span class="p">(</span><span class="s">&quot;/LLim&quot;</span><span class="p">,</span> <span class="nb">int</span><span class="p">(</span><span class="n">data</span><span class="o">.</span><span class="n">LLim</span><span class="p">))</span></div><div class='line' id='LC253'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rospy</span><span class="o">.</span><span class="n">set_param</span><span class="p">(</span><span class="s">&quot;/RLim&quot;</span><span class="p">,</span> <span class="nb">int</span><span class="p">(</span><span class="n">data</span><span class="o">.</span><span class="n">RLim</span><span class="p">))</span></div><div class='line' id='LC254'><br/></div><div class='line' id='LC255'><span class="c">################################################################</span></div><div class='line' id='LC256'><span class="k">def</span> <span class="nf">sonarLoop</span><span class="p">():</span></div><div class='line' id='LC257'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># controls sonar message sequence (mtSendData-&gt;, -&gt;mtHeadData, mtSendData-&gt;, -&gt;mtHeadData,... etc. </span></div><div class='line' id='LC258'><br/></div><div class='line' id='LC259'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#rospy.init_node(&#39;sonar&#39;)</span></div><div class='line' id='LC260'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#rospy.Subscriber(&#39;sonar_update&#39;, String, callback)</span></div><div class='line' id='LC261'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rospy</span><span class="o">.</span><span class="n">Subscriber</span><span class="p">(</span><span class="s">&#39;sonar_update&#39;</span><span class="p">,</span> <span class="n">sonar</span><span class="p">,</span> <span class="n">callback</span><span class="p">)</span></div><div class='line' id='LC262'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">global</span> <span class="n">updateFlag</span></div><div class='line' id='LC263'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">global</span> <span class="n">serialPort</span></div><div class='line' id='LC264'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">updateFlag</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC265'><br/></div><div class='line' id='LC266'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">setupSonar</span><span class="p">()</span></div><div class='line' id='LC267'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">serialPort</span><span class="o">.</span><span class="n">flushInput</span><span class="p">()</span></div><div class='line' id='LC268'><br/></div><div class='line' id='LC269'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">while</span> <span class="ow">not</span> <span class="n">rospy</span><span class="o">.</span><span class="n">is_shutdown</span><span class="p">():</span></div><div class='line' id='LC270'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sonarTalker</span><span class="p">()</span></div><div class='line' id='LC271'>	<span class="c"># 1 second recommended in manual (FAQ) - 0.1 seems to work ok on my laptop - NEED TO CHECK PING RETURNS TO MAKE SURE THIS IS THE CASE       </span></div><div class='line' id='LC272'>	<span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mf">0.1</span><span class="p">)</span></div><div class='line' id='LC273'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="n">updateFlag</span></div><div class='line' id='LC274'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sonarListener</span><span class="p">()</span></div><div class='line' id='LC275'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">updateFlag</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span></div><div class='line' id='LC276'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&#39;HELLO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!&#39;</span></div><div class='line' id='LC277'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">setupData</span> <span class="o">=</span> <span class="n">get_mtHeadCommand</span><span class="p">()</span></div><div class='line' id='LC278'>	    <span class="n">serialPort</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">setupData</span><span class="p">)</span></div><div class='line' id='LC279'>&nbsp;	    <span class="n">updateFlag</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span></div><div class='line' id='LC280'><br/></div><div class='line' id='LC281'><span class="k">def</span> <span class="nf">shutdown</span><span class="p">():</span></div><div class='line' id='LC282'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">global</span> <span class="n">serialPort</span></div><div class='line' id='LC283'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">serialPort</span><span class="o">.</span><span class="n">flushInput</span><span class="p">()</span></div><div class='line' id='LC284'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">serialPort</span><span class="o">.</span><span class="n">flushOutput</span><span class="p">()</span></div><div class='line' id='LC285'><br/></div><div class='line' id='LC286'><br/></div><div class='line' id='LC287'><span class="c">################################################################</span></div><div class='line' id='LC288'><span class="c">################################################################</span></div><div class='line' id='LC289'><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span></div><div class='line' id='LC290'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#needs updating once message structure is sorted...</span></div><div class='line' id='LC291'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rospy</span><span class="o">.</span><span class="n">init_node</span><span class="p">(</span><span class="s">&#39;sonar&#39;</span><span class="p">)</span></div><div class='line' id='LC292'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#rospy.Subscriber(&#39;sonar_update&#39;, String, callback)</span></div><div class='line' id='LC293'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">global</span> <span class="n">updateFlag</span></div><div class='line' id='LC294'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">updateFlag</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC295'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rospy</span><span class="o">.</span><span class="n">on_shutdown</span><span class="p">(</span><span class="n">shutdown</span><span class="p">)</span></div><div class='line' id='LC296'><br/></div><div class='line' id='LC297'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#setupSonar()</span></div><div class='line' id='LC298'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#serialPort.flushInput()</span></div><div class='line' id='LC299'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sonarLoop</span><span class="p">()</span>    </div><div class='line' id='LC300'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC301'><br/></div></pre></div>
              
            
          </td>
        </tr>
      </table>
    
  </div>


          </div>
        </div>
      </div>
    </div>
  

  </div>


<div class="frame frame-loading" style="display:none;">
  <img src="https://a248.e.akamai.net/assets.github.com/images/modules/ajax/big_spinner_336699.gif" height="32" width="32">
</div>

    </div>
  
      
    </div>

    <!--**************
     FOOTER
     **************-->
    <div id="footer" >
      <div class="upper_footer">
        <div class="site" class="clearfix">

        <!--[if IE]><h4 id="blacktocat_ie">GitHub Links</h4><![endif]-->
        <![if !IE]><h4 id="blacktocat">GitHub Links</h4><![endif]>

        <ul class="footer_nav">
          <h4>GitHub</h4>
          <li><a href="https://github.com/about">About</a></li>
          <li><a href="https://github.com/blog">Blog</a></li>
          <li><a href="https://github.com/contact">Contact &amp; Support</a></li>
          <li><a href="https://github.com/training">Training</a></li>
          <li><a href="http://status.github.com/">Site Status</a></li>
        </ul>

        <ul class="footer_nav">
          <h4>Tools</h4>
          <li><a href="http://mac.github.com/">GitHub for Mac</a></li>
          <li><a href="http://mobile.github.com/">GitHub:Issues for iPhone</a></li>
          <li><a href="https://gist.github.com">Gist: Code Snippets</a></li>
          <li><a href="http://fi.github.com/">Enterprise Install</a></li>
          <li><a href="http://jobs.github.com/">Job Board</a></li>
        </ul>

        <ul class="footer_nav">
          <h4>Extras</h4>
          <li><a href="http://shop.github.com/">GitHub Shop</a></li>
          <li><a href="http://octodex.github.com/">The Octodex</a></li>
        </ul>

        <ul class="footer_nav">
          <h4>Documentation</h4>
          <li><a href="http://help.github.com/">GitHub Help</a></li>
          <li><a href="http://developer.github.com/">Developer API</a></li>
          <li><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></li>
          <li><a href="http://pages.github.com/">GitHub Pages</a></li>
        </ul>

        </div><!-- /.site -->
      </div><!-- /.upper_footer -->

      <div class="lower_footer">
        <div class="site" class="clearfix">

        <!--[if IE]><div id="legal_ie"><![endif]-->
        <![if !IE]><div id="legal"><![endif]>
              <ul>
                <li><a href="https://github.com/site/terms">Terms of Service</a></li>
                <li><a href="https://github.com/site/privacy">Privacy</a></li>
                <li><a href="https://github.com/security">Security</a></li>
              </ul>

              <p>&copy; 2011 <span id="_rrt" title="0.14700s from fe5.rs.github.com">GitHub</span> Inc. All rights reserved.</p>
            </div><!-- /#legal or /#legal_ie-->

          
          <div class="sponsor">
              <a href="http://www.rackspace.com" class="logo">
                <img alt="Dedicated Server" height="36" src="https://a248.e.akamai.net/assets.github.com/images/modules/footer/rackspace_logo.png?v2" width="38" />
              </a>
              Powered by the <a href="http://www.rackspace.com ">Dedicated
              Servers</a> and<br/> <a href="http://www.rackspacecloud.com">Cloud
              Computing</a> of Rackspace Hosting<span>&reg;</span>
          </div>
          
        </div><!-- /.site -->
      </div><!-- /.lower_footer -->
    </div><!-- /#footer -->

    

<div id="keyboard_shortcuts_pane" class="instapaper_ignore readability-extra" style="display:none">
  <h2>Keyboard Shortcuts <small><a href="#" class="js-see-all-keyboard-shortcuts">(see all)</a></small></h2>

  <div class="columns threecols">
    <div class="column first">
      <h3>Site wide shortcuts</h3>
      <dl class="keyboard-mappings">
        <dt>s</dt>
        <dd>Focus site search</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>?</dt>
        <dd>Bring up this help dialog</dd>
      </dl>
    </div><!-- /.column.first -->

    <div class="column middle" style='display:none'>
      <h3>Commit list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selected down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selected up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>t</dt>
        <dd>Open tree</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>p</dt>
        <dd>Open parent</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>c <em>or</em> o <em>or</em> enter</dt>
        <dd>Open commit</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>y</dt>
        <dd>Expand URL to its canonical form</dd>
      </dl>
    </div><!-- /.column.first -->

    <div class="column last" style='display:none'>
      <h3>Pull request list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selected down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selected up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>o <em>or</em> enter</dt>
        <dd>Open issue</dd>
      </dl>
    </div><!-- /.columns.last -->

  </div><!-- /.columns.equacols -->

  <div style='display:none'>
    <div class="rule"></div>

    <h3>Issues</h3>

    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>j</dt>
          <dd>Move selected down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>k</dt>
          <dd>Move selected up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>x</dt>
          <dd>Toggle select target</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o <em>or</em> enter</dt>
          <dd>Open issue</dd>
        </dl>
      </div><!-- /.column.first -->
      <div class="column middle">
        <dl class="keyboard-mappings">
          <dt>I</dt>
          <dd>Mark selected as read</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>U</dt>
          <dd>Mark selected as unread</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>e</dt>
          <dd>Close selected</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>y</dt>
          <dd>Remove selected from view</dd>
        </dl>
      </div><!-- /.column.middle -->
      <div class="column last">
        <dl class="keyboard-mappings">
          <dt>c</dt>
          <dd>Create issue</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>l</dt>
          <dd>Create label</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>i</dt>
          <dd>Back to inbox</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>u</dt>
          <dd>Back to issues</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>/</dt>
          <dd>Focus issues search</dd>
        </dl>
      </div>
    </div>
  </div>

  <div style='display:none'>
    <div class="rule"></div>

    <h3>Network Graph</h3>
    <div class="columns equacols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt><span class="badmono">←</span> <em>or</em> h</dt>
          <dd>Scroll left</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">→</span> <em>or</em> l</dt>
          <dd>Scroll right</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">↑</span> <em>or</em> k</dt>
          <dd>Scroll up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">↓</span> <em>or</em> j</dt>
          <dd>Scroll down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>t</dt>
          <dd>Toggle visibility of head labels</dd>
        </dl>
      </div><!-- /.column.first -->
      <div class="column last">
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">←</span> <em>or</em> shift h</dt>
          <dd>Scroll all the way left</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">→</span> <em>or</em> shift l</dt>
          <dd>Scroll all the way right</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">↑</span> <em>or</em> shift k</dt>
          <dd>Scroll all the way up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">↓</span> <em>or</em> shift j</dt>
          <dd>Scroll all the way down</dd>
        </dl>
      </div><!-- /.column.last -->
    </div>
  </div>

  <div >
    <div class="rule"></div>
    <div class="columns threecols">
      <div class="column first" >
        <h3>Source Code Browsing</h3>
        <dl class="keyboard-mappings">
          <dt>t</dt>
          <dd>Activates the file finder</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>l</dt>
          <dd>Jump to line</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>y</dt>
          <dd>Expand URL to its canonical form</dd>
        </dl>
      </div>
    </div>
  </div>
</div>

    <div id="markdown-help" class="instapaper_ignore readability-extra">
  <h2>Markdown Cheat Sheet</h2>

  <div class="cheatsheet-content">

  <div class="mod">
    <div class="col">
      <h3>Format Text</h3>
      <p>Headers</p>
      <pre>
# This is an &lt;h1&gt; tag
## This is an &lt;h2&gt; tag
###### This is an &lt;h6&gt; tag</pre>
     <p>Text styles</p>
     <pre>
*This text will be italic*
_This will also be italic_
**This text will be bold**
__This will also be bold__

*You **can** combine them*
</pre>
    </div>
    <div class="col">
      <h3>Lists</h3>
      <p>Unordered</p>
      <pre>
* Item 1
* Item 2
  * Item 2a
  * Item 2b</pre>
     <p>Ordered</p>
     <pre>
1. Item 1
2. Item 2
3. Item 3
   * Item 3a
   * Item 3b</pre>
    </div>
    <div class="col">
      <h3>Miscellaneous</h3>
      <p>Images</p>
      <pre>
![GitHub Logo](/images/logo.png)
Format: ![Alt Text](url)
</pre>
     <p>Links</p>
     <pre>
http://github.com - automatic!
[GitHub](http://github.com)</pre>
<p>Blockquotes</p>
     <pre>
As Kanye West said:
> We're living the future so
> the present is our past.
</pre>
    </div>
  </div>
  <div class="rule"></div>

  <h3>Code Examples in Markdown</h3>
  <div class="col">
      <p>Syntax highlighting with <a href="http://github.github.com/github-flavored-markdown/" title="GitHub Flavored Markdown" target="_blank">GFM</a></p>
      <pre>
```javascript
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```</pre>
    </div>
    <div class="col">
      <p>Or, indent your code 4 spaces</p>
      <pre>
Here is a Python code example
without syntax highlighting:

    def foo:
      if not bar:
        return true</pre>
    </div>
    <div class="col">
      <p>Inline code for comments</p>
      <pre>
I think you should use an
`&lt;addr&gt;` element here instead.</pre>
    </div>
  </div>

  </div>
</div>
    

    <!--[if IE 8]>
    <script type="text/javascript" charset="utf-8">
      $(document.body).addClass("ie8")
    </script>
    <![endif]-->

    <!--[if IE 7]>
    <script type="text/javascript" charset="utf-8">
      $(document.body).addClass("ie7")
    </script>
    <![endif]-->

    
    
    
    <script type="text/javascript">(function(){var d=document;var e=d.createElement("script");e.async=true;e.src="https://d1ros97qkrwjf5.cloudfront.net/16/eum/rum.js	";e.type="text/javascript";var s=d.getElementsByTagName("script")[0];s.parentNode.insertBefore(e,s);})();NREUMQ.push(["nrf2","beacon-1.newrelic.com","2f94e4d8c2",64799,"dw1bEBZcX1RWRhoEClsAGhcMXEQ=",0,142,new Date().getTime()])</script>
  </body>
</html>

