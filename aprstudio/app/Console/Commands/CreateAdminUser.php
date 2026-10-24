<?php

namespace App\Console\Commands;

use App\Models\User;
use Illuminate\Console\Command;
use Illuminate\Database\QueryException;

class CreateAdminUser extends Command
{
    /**
     * The name and signature of the console command.
     *
     * @var string
     */
    protected $signature = 'create:admin_user';

    /**
     * The console command description.
     *
     * @var string
     */
    protected $description = 'Create an Admin User';

    /**
     * Create a new command instance.
     *
     * @return void
     */
    public function __construct()
    {
        parent::__construct();
    }

    /**
     * Execute the console command.
     *
     * @return int
     */
    public function handle()
    {
        $name = $this->ask('Name');
        $email = $this->ask('Email');
        $password = $this->secret('Password');
        $confirm_password = $this->secret('Confirm Password');

        if ($password != $confirm_password) {
            $this->error('Passwords did not match.');
            return 0;
        }

        if ($this->confirm('Do you wish to continue?')) {
            $user = new User([
                'name' => $name,
                'email' => $email
            ]);
            $user->set_password($password);
            $user->is_admin = true;

            try {
                $user->save();
            } catch (QueryException $e) {
                $this->error('This email is already taken.');
                return 0;
            }

            $this->info("Admin User {name} created successfully.");
        } else {
            $this->info('Cancelled.');
        }
        return 0;
    }
}
