/*
* ALT MENU
*/

(function(){
	
	/*
	Scene_MenuBase.prototype.createBackground = function() {
		this._backgroundSprite = new Sprite();
		this._backgroundSprite.bitmap = ImageManager.loadPicture("blue_brain");
		this.addChild(this._backgroundSprite);
		this._backgroundSprite.y = Graphics.boxHeight/3.8;
	};
	*/

	var _Scene_Menu_create = Scene_Menu.prototype.create;

	Scene_Menu.prototype.create = function() {
		
		_Scene_Menu_create.call(this);
		//Scene_MenuBase.prototype.create.call(this);
		//this.createCommandWindow();
		//this.createGoldWindow();
		//this.createStatusWindow();
		
		/*
		this._commandWindow;
		this._goldWindow;
		this._statusWindow;
		*/
		
		this._statusWindow.x = 0;
		this._statusWindow.y = 0;
		
		
		this._commandWindow.y = this._statusWindow.height;
		this._commandWindow.x = 0;
		//this._commandWindow.x = this._statusWindow.width/2;
		
		//this._goldWindow.x = this._statusWindow.width/2;
		//this._goldWindow.y = this._commandWindow.height/2;
		
	};

	Window_MenuStatus.prototype.windowWidth = function() {
		return Graphics.boxWidth;
	};

	Window_MenuStatus.prototype.windowHeight = function() {
		return Graphics.boxHeight/3.5;
	};
	Window_MenuStatus.prototype.numVisibleRows = function() {
		return 1;
	};
	Window_MenuStatus.prototype.maxCols = function() {
		return 2;
	};
	Window_MenuCommand.prototype.windowWidth = function() {
		return 200;
		//return Graphics.boxWidth;
	};
	Window_MenuCommand.prototype.windowHeight = function() {
		//return this.fittingHeight(this.numVisibleRows());
		//return Graphics.boxHeight/1.394;
		return Graphics.boxHeight/5.5;
	};
	Window_MenuCommand.prototype.numVisibleRows = function() {
		return this.maxItems();
	};
	Window_MenuCommand.prototype.maxCols = function() {
		return 1;
	};
	
	Window_MenuCommand.prototype.itemTextAlign = function() {
		return 'center';
	};
	

	
	
	
})();